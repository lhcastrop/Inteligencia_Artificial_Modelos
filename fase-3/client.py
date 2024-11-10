
import requests
import time
import os
import pandas as pd
def train_model():
    response = requests.post('http://localhost:5000/train')
    #print(response.json())
    
    # Esperar un momento para que el modelo se guarde
    time.sleep(10)
    
    # Verificar si el modelo fue guardado
    if os.path.exists('models/model.pkl'):
        print("Modelo guardado en models/model.pkl")
    else:
        print("El modelo no se guardó correctamente.")

def predict(data):
    response = requests.post('http://localhost:5000/predict', json={'input': data})
    
    # Verificar si las predicciones fueron guardadas
    if os.path.exists('predictions/test_predictions.csv'):
        print("Predicciones guardadas en predictions/test_predictions.csv")
    else:
        print("Las predicciones no se guardaron correctamente.")

if __name__ == '__main__':
    # Entrenar el modelo
    train_model()

    # Leer los datos de entrada desde test_data_input.csv
    input_df = pd.read_csv('test_data_input.csv')
    input_data = input_df.to_dict(orient='records')  # Convertir a lista de diccionarios

    # Predecir usando los datos cargados
    predict(input_data)

