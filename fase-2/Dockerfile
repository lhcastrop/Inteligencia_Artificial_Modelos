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

# Copia los archivos necesarios
COPY requirements.txt ./
COPY train.py ./
COPY predict.py ./

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Comando por defecto
CMD ["python", "train.py"]
