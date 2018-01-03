# bergi

e-bergi is a tech blog which resides [here](http://e-bergi.com).

## run

To take a look around with a slice of the data,

```
pip3 install -r requirements.txt
./manage.py migrate
tar xzf last_known_ok.tar.gz
./manage.py loaddata last_known_ok
./manage.py runserver
```

## contribute

bergi is mostly straightforward if you know Django. If you don't, it will become straightforward after you read the Django [tutorials](https://docs.djangoproject.com/en/1.11/intro/tutorial01/).

You can get started by looking at the [urls.py](_bergi/urls.py) file to see what URL points to what.

A list of issues to tackle are in the [issue tracker](https://github.com/duck2/bergi/issues).
