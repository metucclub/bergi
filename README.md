# bergi

bergi is python-kosher name for e-bergi.

e-bergi is a tech blog which resides [here](http://e-bergi.com).

This repo is a straightforward Django setup to replace it.

## watch

[bergi.duck2.lt](http://bergi.duck2.lt) should be running the git repository.

## run

Migrations are not yet committed since the schema is likely to change.

To take a look around with dummy [data](_bergi/fixtures/dummy.json),

```
pip3 install -r requirements.txt
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
		- [x] aside
		- [x] nav
			- [x] ~~which cats to put on nav?~~ chosen ones
			- [x] icons
				- [ ] strip font-awesome
			- [x] what else to put
				- [x] "about"
				- [ ] "archives"
		- [ ] footer
	- [ ] [author](_bergi/templates/author.html)
	- [ ] [article](_bergi/templates/article.html)
		- [x] sheet
		- [x] recommends
			- [ ] better recommendation algorithm?
		- [ ] author box
		- [ ] comments
	- [ ] [cat](_bergi/templates/cat.html)

- [ ] misc
	- [ ] tags
	- [ ] archives
		- [ ] pagination for archives?
	- [ ] about


- [ ] cms
