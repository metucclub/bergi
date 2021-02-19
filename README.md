# bergi

e-bergi is a tech blog which resides [here](http://e-bergi.com).

## run

#### Method 1:

Install [Docker](https://docs.docker.com/install/) and [docker-compose](https://docs.docker.com/compose/install/), then run:

```
# docker-compose up
```

It will set up a network with bergi, PostgreSQL and Elasticsearch and expose an e-bergi instance to port 8000. You can open a shell in the django-running container with `docker-compose exec app bash`.

#### Method 2:

bergi expects a PostgreSQL server listening on localhost:5432 and an Elasticsearch cluster listening on localhost:9200. After setting those services up, in a virtualenv or outside if you are feeling generous, run:

```
pip3 install -r requirements.txt
./manage.py migrate
./manage.py runserver
```

## contribute

bergi is mostly straightforward if you know Django. If you don't, it will become straightforward after you read the Django [tutorials](https://docs.djangoproject.com/en/2.2/intro/tutorial01/).

You can get started by looking at the [urls.py](_bergi/urls.py) file to see what URL points to what.

A list of issues to tackle are in the [issue tracker](https://github.com/metucclub/bergi/issues).
