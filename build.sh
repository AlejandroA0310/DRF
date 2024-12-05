#!/usr/bin/env bash
# exit on error
set -0 errexit

poetry install

python manage.py collectstatic --no-input
python manage.py migrate