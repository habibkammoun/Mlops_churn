FROM --platform=linux/amd64 python:3.10

WORKDIR /app

COPY requirements.txt .
RUN pip install  -r requirements.txt

COPY . .

# Définir une variable d'environnement par défaut
#ENV PORT 8080

# Exposer le port par défaut
#EXPOSE 8080

CMD gunicorn -w 3 -k uvicorn.workers.UvicornWorker main:app --bind 0.0.0.0:$PORT
