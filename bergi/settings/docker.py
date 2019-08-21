import os
from .base import *

DEBUG = False

ALLOWED_HOSTS = ['e-bergi.com', 'www.e-bergi.com', 'ebergi.com', 'www.ebergi.com']

DATABASES = {
    "default": {
		"ENGINE": "django.db.backends.postgresql_psycopg2",
		"NAME": os.environ.get("db_name"),
		"USER": os.environ.get("db_user"),
		"HOST": os.environ.get("db_host"),
    }
}

ES_HOSTS = [os.environ.get("elasticsearch_host") + ":9200"]
