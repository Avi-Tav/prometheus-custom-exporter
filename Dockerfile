FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8222

ENV LOG_LEVEL=INFO \
    LISTENING_PORT=8222 \
    INTERVAL_MYJOB_SECONDS=30 \
    BASE_SERVER_URL=https://www.google.com/ \
    SKIP_MONITOR_CHECK=false

CMD ["python", "main.py"]
