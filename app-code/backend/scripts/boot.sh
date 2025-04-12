#!/bin/bash
set -e
# Apply migrations
# python manage.py makemigrations --noinput
python manage.py makemigrations
python manage.py migrate
gunicorn filemanager.wsgi:application --bind 0.0.0.0:8000



