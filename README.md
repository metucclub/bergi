# bergi

bergi is python-kosher name for e-bergi.

e-bergi is a tech blog which resides [here](http://e-bergi.com).

This repo is a Django setup to replace it.

## watch

[bergi.duck2.lt](http://bergi.duck2.lt) should be running the git repository.

## run

Migrations are not yet committed since the schema is likely to change.

To take a look around with dummy [data](_bergi/fixtures/dummy.json),

```
pip3 install -r requirements.txt
./manage.py makemigrations _bergi
./manage.py migrate
./manage.py loaddata dummy
./manage.py runserver
```

We have two 2015 issues in the repository too. Load their data with `loaddata last_known_ok`.

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
		- [x] aside
		- [x] nav
			- [x] ~~which cats to put on nav?~~ chosen ones
			- [x] icons
				- [ ] strip font-awesome
			- [x] what else to put
				- [x] "about"
				- [x] "archives"
		- [x] footer
	- [x] [author](_bergi/templates/author.html)
	- [x] [article](_bergi/templates/article.html)
		- [x] sheet
		- [x] recommends
			- [ ] better recommendation algorithm?
		- [ ] author box
		- [ ] share buttons
		- [ ] comments
	- [x] [cat](_bergi/templates/cat.html)

- [ ] misc
	- [ ] tags
	- [x] archives
		- [x] pagination for archives?
	- [ ] about

- [ ] cms
