FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8080

RUN addgroup --system appgroup && adduser --system --group appuser

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY src/ .

RUN chown -R appuser:appgroup /app
USER appuser

EXPOSE 8080

CMD ["python", "app.py"]

