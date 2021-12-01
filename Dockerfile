FROM python:latest

LABEL maintainer="Ignacio Gonzalez Betegon <nachogon92@gmail.com>"

ENV PYTHONPATH=./app

COPY /requirements.txt requirements.txt
COPY /setup.py setup.py

RUN pip install -r requirements.txt && pip install --editable .

EXPOSE 8000

COPY . .