from django.urls import include, path

from . import views

urlpatterns = [
	path("", views.index),
	path("yazar/<slug:slug>/", views.author, name="author"),
	path("y/<slug:slug>/", views.article, name="article"),
	path("kat/<slug:slug>/", views.cat),
	path("kat/<slug:slug>/<int:page>", views.cat, name="cat"),
	path("arsiv/", views.archive),
	path("arsiv/<int:page>", views.archive, name="archive"),
	path("hakkinda/", views.about, name="about"),
	path("kunye/", views.team, name="team"),
	path("ara/", views.search, name="search"),
]
