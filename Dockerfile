FROM python:latest

LABEL maintainer="Ignacio Gonzalez Betegon <nachogon92@gmail.com>"

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY /requirements.txt requirements.txt
COPY /setup.py setup.py

RUN pip install --upgrade pip
RUN pip install -r requirements.txt && pip install --editable .

EXPOSE 8000

ENV PYTHONPATH=./app