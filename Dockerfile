# Dockerfile
FROM python:3.10-slim

# Instalar dependencias básicas
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Crear directorio de trabajo
WORKDIR /app

# Copiar requerimientos
COPY requirements.txt .

# Instalar dependencias
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copiar código
COPY . .

# Puerto de Streamlit
EXPOSE 8501

# Comando por defecto
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
