#!/bin/sh

# Prepare log files and start outputting logs to stdout
mkdir /srv/logs
touch /srv/logs/gunicorn.log
touch /srv/logs/access.log
tail -n 0 -f /srv/logs/*.log &

cd src

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn core.wsgi:application \
    --name articlemetrics \
    --bind 0.0.0.0:8888 \
    --workers 3 \
    --log-level=info \
    --log-file=/srv/logs/gunicorn.log \
    --access-logfile=/srv/logs/access.log \
    "$@"
