from flask import Flask, request, jsonify
import subprocess
import pandas as pd
import os

app = Flask(__name__)

# Define las rutas para los archivos
MODEL_FILE = 'models/model.pkl'  # Ruta para el modelo
TRAIN_DATA_FILE = 'train.csv'  # Ruta para los datos de entrenamiento
TEST_INPUT_FILE = 'test_data_input.csv'  # Ruta para los datos de entrada
TEST_TARGET_FILE = 'test_data_target.csv'  # Ruta para los resultados esperados
TEST_PREDS_FILE = 'predictions/test_predictions.csv'  # Ruta para las predicciones

@app.route('/train', methods=['POST'])
def train():
    try:
        subprocess.run(['python', 'train.py', '--data_file', TRAIN_DATA_FILE, '--model_file', MODEL_FILE], check=True)
        return jsonify({"message": "Entrenamiento completado satisfactoriamente!"}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({"error": str(e)}), 500

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    if 'input' not in data:
        return jsonify({"error": "Los datos de entrada son requeridos"}), 400

    input_data = data['input']
    pd.DataFrame(input_data).to_csv(TEST_INPUT_FILE, index=False)

    try:
        subprocess.run(['python', 'predict.py',
                        '--input_file', TEST_INPUT_FILE,
                        '--predictions_file', TEST_PREDS_FILE,
                        '--model_file', MODEL_FILE], check=True)

        # Verifica si el archivo de predicciones se creó correctamente
        if not os.path.isfile(TEST_PREDS_FILE):
            return jsonify({"error": "No se encontro el archivo de predicciones!"}), 500

        predictions = pd.read_csv(TEST_PREDS_FILE)
        return jsonify(predictions.to_dict(orient='records')), 200
    except subprocess.CalledProcessError as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
