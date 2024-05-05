FROM python:alpine3.19

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 5000

# Comando para ejecutar la aplicación
ENTRYPOINT ["python","./main.py","flask","host=0.0.0.0","port=5000"]