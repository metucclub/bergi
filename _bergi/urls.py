from django.conf.urls import include, url
from django.views.generic import RedirectView
from django.core.urlresolvers import reverse_lazy

from . import views

urlpatterns = [
	url(r"^$", views.index),
	url(r"^yazar/([-a-z0-9]+)/$", views.author, name="author"),
	url(r"^y/([-_a-z0-9]+)/$", views.article, name="article"),
	url(r"^y/([-_a-zA-Z0-9]+)/$", views.irregular_article, name="irregular_article"),
	url(r"^kat/([-a-z0-9]+)/([0-9]*)/?$", views.cat, name="cat"),
	url(r"^arsiv/([0-9]*)/?$", views.archive, name="archive"),
	url(r"^ara/$", views.search, name="search"),
]
