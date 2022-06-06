FROM python:3

RUN apt-get update -y && \
  apt-get install -y python3-pip python-dev

WORKDIR /app

RUN pip install Flask requests flask_mysqldb

COPY . .

CMD ["python", "./atm.py"]