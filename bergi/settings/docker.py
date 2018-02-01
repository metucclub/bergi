from .base import *

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
