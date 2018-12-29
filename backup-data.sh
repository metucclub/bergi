#!/bin/sh

timestamp=$(date +%s)

if [ ! -z "$1" ]; then
	filename="db.zip"
else
	filename="db_$timestamp.zip"
fi

python manage.py dumpdata -e contenttypes -e auth.Permission  --exclude admin.LogEntry --exclude sessions > db.json

zip -q -r "$filename" media db.json

rm db.json