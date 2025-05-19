FROM python:3.10.5-slim

WORKDIR /app

ENV PORT=5000

COPY dice-app /app

RUN pip install -r ./requirements.txt

EXPOSE ${PORT}

ENTRYPOINT ["sh", "-c", "gunicorn --bind 0.0.0.0:${PORT} app:app"]
