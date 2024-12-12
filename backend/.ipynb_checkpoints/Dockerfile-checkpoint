FROM --platform=linux/amd64 python:3.10
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .  # This copies all files to /app
EXPOSE 8080
CMD gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app --bind 0.0.0.0:${PORT:-8080} --timeout 900