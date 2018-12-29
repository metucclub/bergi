from .base import *

DEBUG = False

ALLOWED_HOSTS = ['0.0.0.0', 'localhost']

DATABASES = {
    'default': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
		'NAME': 'bergi',
		'USER': 'bergi',
		'HOST': 'postgres',
		'PORT': '5432',
    }
}

ES_HOSTS = ["elasticsearch:9200"]
