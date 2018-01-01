from django.conf.urls import include, url

from . import views

urlpatterns = [
	url(r"^$", views.index),
	url(r"^yazar/([-a-z0-9]+)/$", views.author, name="author"),
	url(r"^y/([-_a-z0-9]+)/$", views.article, name="article"),
	url(r"^y/([+-_\w0-9]+)/$", views.irregular_article),
	url(r"^[0-9]{4}/[a-zA-Z]+/([+-_\w0-9]+)/$", views.irregular_article),
	url(r"^kat/([-a-z0-9]+)/([0-9]*)/?$", views.cat, name="cat"),
	url(r"^arsiv/([0-9]*)/?$", views.archive, name="archive"),
	url(r"^hakkinda/$", views.about, name="about"),
	url(r"^kunye/$", views.team, name="team"),
	url(r"^ara/$", views.search, name="search"),
]
