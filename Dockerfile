FROM python:3.6-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ADD . /usr/src/app/

# we have to compile stuff there
RUN apk add --update \
	build-base \
	libffi-dev \
	postgresql-dev \
	libmemcached-dev \
	cyrus-sasl-dev \
	libjpeg-turbo-dev

# no output otherwise
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE bergi.settings.docker

RUN pip install -r requirements.txt

# migrate on start
CMD sh -c "./docker-wait-for.sh postgres:5432 &&\
		./docker-wait-for.sh elasticsearch:9200 &&\
		python3 manage.py migrate &&\
		tar xzf last_known_ok.tar.gz &&\
		echo "yes" | python3 manage.py flush &&\
		python3 manage.py loaddata last_known_ok &&\
		python3 manage.py runserver 0.0.0.0:8000"
