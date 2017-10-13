from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from django.db.models import Q
from django.core.paginator import *

from .models import *

import random

# We need this to put "cats" in global context, so every view doesn't have to call Cat.objects.get for the navigation bar.
# See how it is pipelined in ../bergi/settings.py:/context_processors/ .
def cats_on_navbar(request):
	return {"cats": Cat.objects.filter(on_navbar=True)}

# get_object_or_404 looks like a custom function, but it is a Django shortcut.
def index(request):
	articles = Article.objects.order_by("-date")
	cover = articles[:3]
	river = articles[3:13]
	pop = Article.objects.exclude(pk__in=([o.pk for o in cover]+[o.pk for o in river]))
	ctx = {"cover": cover, "river": river, "pop": pop}
	return render(request, "index.html", ctx)

def author(request, slug):
	author = get_object_or_404(Author, slug=slug)
	ctx = {"author": author,
		"author_articles": author.article_set.order_by("-date")}
	return render(request, "author.html", ctx)

# current recommendation algorithm is ducktape and close to random:
# mix 4 popular articles and articles with same cat or author, draw 4.
def article(request, slug):
	article = get_object_or_404(Article, slug=slug)
	other_articles = Article.objects.exclude(slug=slug)

	# see https://stackoverflow.com/questions/739776
	r = other_articles.filter(Q(cats__in=article.cats.all()) | Q(authors__in=article.authors.all())) | other_articles.order_by("pop")[:4]
	r = list(r.distinct())
	random.shuffle(r)
	recommends = r[:4]

	ctx = {"article": article,
		"recommends": recommends}
	return render(request, "article.html", ctx)

def cat(request, slug):
	ctx = {"cat": get_object_or_404(Cat, slug=slug)}
	return render(request, "cat.html", ctx)

# PageNotAnInteger should mean an empty url like /arsiv/ or /arsiv//.
# see urls.py:/arsiv/ .
def archive(request, page):
	paginator = Paginator(Article.objects.order_by("-date"), per_page=20, orphans=6)
	try:
		articles = paginator.page(page)
	except PageNotAnInteger:
		articles = paginator.page(1)
	except EmptyPage:
		raise Http404

	ctx = {"articles": articles,
		"articles_pop": Article.objects.order_by("-pop")[:4]}
	return render(request, "archive.html", ctx)
