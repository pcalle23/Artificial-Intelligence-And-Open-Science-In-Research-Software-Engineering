FROM python:3.10-slim
#dir tabajo
WORKDIR /app 

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#CPY archivos
COPY . .

#A veces no funciona con 15 segundos (poner 30)
CMD ["sh", "-c", "sleep 30 && python analizador.py && python visualizador.py && pytest"]