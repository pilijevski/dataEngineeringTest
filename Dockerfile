FROM python:3.8-slim

COPY app /app

COPY requirements.txt /requirements.txt

RUN python3 -m pip install -r /requirements.txt

WORKDIR /app

ENV PYTHONPATH="/app"
EXPOSE 8000
ENTRYPOINT hypercorn main:app -b 0.0.0.0:8000