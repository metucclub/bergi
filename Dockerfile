FROM python:3.6-alpine

RUN mkdir /app
WORKDIR /app

# we have to compile stuff there
RUN apk add --update \
	build-base \
	libffi-dev \
	postgresql-dev \
	libmemcached-dev \
	cyrus-sasl-dev \
	libjpeg-turbo-dev \
	python-dev \
	py-pip \
	jpeg-dev \
	zlib-dev

ENV LIBRARY_PATH=/lib:/usr/lib

# no output otherwise
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE bergi.settings.docker

ADD requirements.txt .

RUN pip install -r requirements.txt

ADD . .