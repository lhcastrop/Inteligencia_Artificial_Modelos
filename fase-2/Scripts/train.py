# -*- coding: utf-8 -*-
"""train.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18kJOmnr5B9Nh5H-wzw2Ptt0DKRpSJL7C
"""

from rdkit import Chem
from rdkit.Chem import AllChem
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import average_precision_score
from sklearn.preprocessing import OneHotEncoder

import argparse
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import loguru
from loguru import logger
import os
import pandas as pd
import pickle
import duckdb


parser = argparse.ArgumentParser()
parser.add_argument('--data_file', required=True, type=str, help='a csv file with train data')
parser.add_argument('--model_file', required=True, type=str, help='where the trained model will be stored')
parser.add_argument('--overwrite_model', default=False, action='store_true', help='if sets overwrites the model file if it exists')

args = parser.parse_args()

model_file = args.model_file
data_file  = args.data_file
overwrite = args.overwrite_model

if os.path.isfile(model_file):
    if overwrite:
        logger.info(f"overwriting existing model file {model_file}")
    else:
        logger.info(f"model file {model_file} exists. exitting. use --overwrite_model option")
        exit(-1)

logger.info("loading train data")
#Se manipula la base datos de entrada
con = duckdb.connect()
df = con.query(f"""(SELECT *
                        FROM parquet_scan('{data_file}')
                        WHERE binds = 0
                        ORDER BY random()
                        LIMIT 30000)
                        UNION ALL
                        (SELECT *
                        FROM parquet_scan('{data_file}')
                        WHERE binds = 1
                        ORDER BY random()
                        LIMIT 30000)""").df()
con.close()

# Se convierten los SMILEs en moleculas RDKit
df['molecule'] = df['molecule_smiles'].apply(Chem.MolFromSmiles)

#Se generan las ECFPs (Extended-Conectivity Fingerprints- Huellas Dactilares de Conectividad Extendida)
def generate_ecfp(molecule, radius=2, bits=1024):
    if molecule is None:
        return None
    return list(AllChem.GetMorganFingerprintAsBitVect(molecule, radius, nBits=bits))

df['ecfp'] = df['molecule'].apply(generate_ecfp)

# Se realiza la codificación One-hot a los nombres de las proteinas almacenadas en protein_name
onehot_encoder = OneHotEncoder(sparse_output=False)
protein_onehot = onehot_encoder.fit_transform(df['protein_name'].values.reshape(-1, 1))

# Se combinan las ECFPs y los nombres de la proteinas codificadas
X = [ecfp + protein for ecfp, protein in zip(df['ecfp'].tolist(), protein_onehot.tolist())]
y = df['binds'].tolist()

# Se dividen los datos en conjunto de prueba y entrenamiento
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Se crea y entrena el Modelo Random Forest
logger.info("fitting model")
m = RandomForestClassifier(n_estimators=100, random_state=42)
m.fit(X_train, y_train)
#z = pd.read_csv(data_file).values
#Xtr = z[:,:2]
#ytr = z[:,-1]

logger.info(f"saving model to {model_file}")
with open(model_file, "wb") as f:
    pickle.dump(m, f)