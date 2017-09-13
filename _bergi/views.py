from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import *

import random

# We need this to put "cats" in global context, so every view doesn't have to call Cat.objects.get for the navigation bar.
# See how it is pipelined in ../bergi/settings.py:/context_processors/ .
def cats_on_navbar(request):
	return {"cats": Cat.objects.filter(on_navbar=True)}

# get_object_or_404 looks like a custom function, but it is a Django shortcut.
def index(request):
	ctx = {"articles": Article.objects.order_by("-date"),
		"articles_pop": Article.objects.order_by("pop")}
	return render(request, "index.html", ctx)

def author(request, slug):
	ctx = {"author": get_object_or_404(Author, slug=slug)}
	return render(request, "author.html", ctx)

# suggestions are nice: display articles with the same Cat and/or Author.
# XXX: find a better way to recommend articles
def article(request, slug):
	article = get_object_or_404(Article, slug=slug)
	other_articles = Article.objects.exclude(slug=slug)

	# see https://stackoverflow.com/questions/739776
	r = other_articles.filter(cats__in=article.cats.all()) | other_articles.filter(authors__in=article.authors.all())
	recommends = r.distinct()[:4]

	ctx = {"article": article,
		"recommends": recommends}
	return render(request, "article.html", ctx)

def cat(request, slug):
	ctx = {"cat": get_object_or_404(Cat, slug=slug)}
	return render(request, "cat.html", ctx)
