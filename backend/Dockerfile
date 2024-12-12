FROM --platform=linux/amd64 python:3.10

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080

# CMD ["python", "main.py"]

CMD uvicorn main:app --host 0.0.0.0 --port $PORT --timeout-keep-alive 600

