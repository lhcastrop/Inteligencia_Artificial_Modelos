# Usa una imagen base de Python
FROM python:3.10-slim

# Instala las dependencias del sistema necesarias para RDKit
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    libboost-all-dev \
    libeigen3-dev \
    libopenbabel-dev \
    python3-dev \
    && apt-get clean

# Establece el directorio de trabajo
WORKDIR /app

# Crea directorios para almacenar el modelo y las predicciones
RUN mkdir -p /app/models /app/predictions

# Copia los archivos necesarios
COPY requirements.txt ./
COPY train.py ./
COPY predict.py ./
COPY apirest.py ./
COPY train.csv ./
COPY test_data_input.csv ./
COPY test_data_target.csv ./

# Limpia la caché de pip
#RUN pip cache purge

# Instala las dependencias y se da un timeout de 15 min en caso de la conexion a Internet sea lenta
RUN pip install --no-cache-dir -r requirements.txt --timeout=900



# Expone el puerto del API
EXPOSE 5000

# Comando por defecto
CMD ["python", "apirest.py"]
