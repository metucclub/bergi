# bergi

bergi is python-kosher name for e-bergi.

e-bergi is a tech blog which resides [here](http://e-bergi.com).

This repo is a Django setup to replace it.

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

Here is a rough **roadmap** for anyone who wants to help:

- [x] [models](_bergi/models.py)
	- [x] author
	- [x] article
	- [x] cat(category)

- [x] [views](_bergi/views.py)
	- [x] [index](_bergi/templates/index.html)
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
