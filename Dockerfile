FROM python:3-alpine

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
	jpeg-dev \
	zlib-dev \
	bash \
	zip \
	unzip \
	git \
	nano \
	vim

ENV LIBRARY_PATH=/lib:/usr/lib

# no output otherwise
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE bergi.settings.docker

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN git clone https://github.com/metucclub/docker-scripts && \
	mv docker-scripts/*.sh . && \
	rm -rf docker-scripts && \
	mkdir -p ./db

RUN chmod a+x backup-data.sh restore-data.sh docker-wait-for-it.sh
