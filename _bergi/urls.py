from django.conf.urls import url

from . import views

urlpatterns = [
	url(r"^$", views.index),
	url(r"^yazar/([-a-z0-9]+)/$", views.author, name="author"),
	url(r"^y/([-a-z0-9]+)/$", views.article, name="article"),
	url(r"^kat/([-a-z0-9]+)/([0-9]*)/?$", views.cat, name="cat"),
	url(r"^arsiv/([0-9]*)/?$", views.archive, name="archive"),
]
