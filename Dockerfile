FROM python:3.10-slim
#dir tabajo
WORKDIR /app 

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#CPY archivos
COPY . .

CMD ["python", "main.py"]
