FROM python:3.10-alpine3.15

RUN apk update
RUN apk add\
    py-pip \
    gcc \
    build-base \
    # python-dev \
    mariadb-dev \
    libxml2-dev \
    libxslt-dev

COPY requirements.txt /usr/src/app/
WORKDIR /usr/src/app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN export PATH=$PATH:/usr/local/mysql/bin

COPY src src
COPY ./docker-entrypoint.sh /

EXPOSE 8888

ENV DJANGO_SETTINGS_MODULE=core.docker_settings

ENTRYPOINT ["/docker-entrypoint.sh"]
