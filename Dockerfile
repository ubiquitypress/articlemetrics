FROM python:2.7.13-alpine

COPY requirements.txt /usr/src/app/
WORKDIR /usr/src/app

RUN apk update
RUN apk add\
    py-pip \
    gcc \
    build-base \
    python-dev \
    mariadb-dev

RUN pip install -r requirements.txt
RUN export PATH=$PATH:/usr/local/mysql/bin
RUN pip install mysql-python

COPY src src

EXPOSE 8000

WORKDIR src

ENV DJANGO_SETTINGS_MODULE=core.live_settings
CMD ["python", "manage.py", "runserver"]