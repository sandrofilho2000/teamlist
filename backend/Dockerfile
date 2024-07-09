FROM python:3.12-bookworm

ENV PYTHONBUFFERD = 1

WORKDIR /django

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . . 

CMD gunicorn setup.wsgi:application --bind 0.0.0.0:8000

EXPOSE 8000