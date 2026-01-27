FROM python:3.12-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1

COPY requirements.txt .

RUN pip install -r requirements.txt


CMD ["opentelemetry-instrument", "--otel_exporter_otlp_endpoint", "http://alloy:4317", "python", "manage.py", "runserver", "0.0.0.0:8000"]