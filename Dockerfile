FROM python:latest

LABEL maintainer="Ignacio Gonzalez Betegon <nachogon92@gmail.com>"

ENV PYTHONPATH=.

RUN pip install virtualenv

COPY /requirements.txt requirements.txt

RUN pip install -r requirements.txt

EXPOSE 8000

COPY . .

CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]