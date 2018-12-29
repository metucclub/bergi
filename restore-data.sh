#!/bin/sh

if [ ! -z "$1" ]; then
    unzip -q -o $1

    python manage.py loaddata db.json

    rm db.json
else
    echo "Please define a filename"
fi