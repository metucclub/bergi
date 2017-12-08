# bergi

e-bergi is a tech blog which resides [here](http://e-bergi.com).

## watch

[bergi.duck2.lt](http://bergi.duck2.lt) should be running the git repository.

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

Here is a list of issues:

- [ ] font-awesome is too big, we will need to throw out unused parts of it.
- [ ] Some images are >1MB but only displayed 300x200. We are going to need Thumbnails or an image endpoint which delivers small or big.
- [ ] The recommendation algorithm is ducktape. We need "More like this" functionality, or at least an exp(-Wt) function which throws old articles back.
- [ ] The article page is somewhat dull. What about augmenting with share buttons and an author box at the article tail?
- [ ] Comments for articles could be nice.
- [ ] Do our articles need _tags_?
- [ ] Articles don't write themselves. We need a [content management system](https://www.wikiwand.com/en/Content_management_system) to manage the workflow.
