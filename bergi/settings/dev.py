import os
from .base import *

DATABASES = {
    "default": {
		"ENGINE": "django.db.backends.postgresql_psycopg2",
		"NAME": os.environ.get("db_name"),
		"USER": os.environ.get("db_user"),
		"HOST": os.environ.get("db_host"),
		"PASSWORD": os.environ.get("db_pass"),
    }
}

ES_HOSTS = [os.environ.get("elasticsearch_host") + ":9200"]
