#!/bin/sh

# Prepare log files and start outputting logs to stdout
mkdir /srv/logs
touch /srv/logs/gunicorn.log
touch /srv/logs/access.log
tail -n 0 -f /srv/logs/*.log &

python src/manage.py runserver 0:8000