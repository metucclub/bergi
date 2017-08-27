# bergi

bergi is python-kosher name for e-bergi.

e-bergi is a tech blog which resides [here](http://e-bergi.com).

This repo is a straightforward Django setup to replace it.

## watch

[duck2.lt/e-bergi/](http://duck2.lt/e-bergi/) ~~runs~~ is going to run the git repository.

## run

Migrations are not yet committed since the schema is likely to change.

To take a look around with dummy [data](_bergi/fixtures/dummy.json),

```
./manage.py makemigrations
./manage.py migrate
./manage.py loaddata dummy
./manage.py runserver
```

## contribute

Here is a rough **roadmap** for anyone who wants to help:

- [x] [models](_bergi/models.py)
	- [x] author
	- [x] article
	- [x] cat(category)

- [x] [views](_bergi/views.py)
	- [ ] [index](_bergi/templates/index.html)
		- [x] cover
		- [x] content river
		- [ ] nav
	- [ ] [author](_bergi/templates/author.html)
	- [ ] [article](_bergi/templates/article.html)
	- [ ] [cat](_bergi/templates/cat.html)

- [ ] cms

- [ ] misc
	- [ ] tags
	- [ ] archives
		- [ ] pagination for archives?
