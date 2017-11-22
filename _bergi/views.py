from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.template.defaultfilters import slugify

from django.db.models import Q
from django.core.paginator import *

from .models import *

import random

# We need this to put "cats" in global context, so every view doesn't have to call Cat.objects.get for the navigation bar.
# See how it is pipelined in ../bergi/settings/base.py:/context_processors/ .
def cats_on_navbar(request):
	return {"cats": Cat.objects.filter(on_navbar=True)}

# get_object_or_404 looks like a custom function, but it is a Django shortcut.
# we don't place any post in Pop if it's already on the page.
def index(request):
	articles = Article.objects.order_by("-date")
	cover = articles[:3]
	river = articles[3:13]
	pop = Article.objects.exclude(pk__in=([o.pk for o in cover]+[o.pk for o in river]))[:4]
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

# we have legacy articles with non-conforming slugs
# tame them by redirecting permanently
def irregular_article(request, raw_slug):
	slug = slugify(raw_slug)
	return redirect("article", slug, permanent=True)

# generic fn to use with paginated views.
# returns a context with the Page obj,
# a range for templates/_paginator.html and whether to show ellipses(…).
def page_ctx(paginator, page):
	try:
		page = paginator.page(page)
	except PageNotAnInteger:
		page = paginator.page(1)
	except EmptyPage:
		raise Http404

	n = page.number+1
	N = paginator.num_pages

	left = max(2, n-2)
	right = min(n+2, N)

	return {"page_obj": page,
		"range": range(left, right),
		"left_ellipsis": left > 2,
		"right_ellipsis": right < N}

# PageNotAnInteger should mean an empty url like /arsiv/ or /arsiv//.
# see urls.py:/arsiv/ .
def archive(request, page):
	paginator = Paginator(Article.objects.order_by("-date"), per_page=100, orphans=1)

	ctx = page_ctx(paginator, page)
	return render(request, "archive.html", ctx)

def cat(request, slug, page):
	cat = get_object_or_404(Cat, slug=slug)
	paginator = Paginator(cat.article_set.order_by("-date"), per_page=100, orphans=1)

	ctx = page_ctx(paginator, page)
	ctx["cat"] = cat

	return render(request, "cat.html", ctx)

# __search is a Postgres feature.
# we check for it and provide a fallback for dev environments
# XXX: remove magic number 10

from django.db import connection
if connection.vendor == "postgresql":
	def lkup(key):
		return Article.objects.filter(content__search=key)[:10]
else:
	def lkup(key):
		return Article.objects.filter(content__icontains=key)[:10]

def lookup(key):
	if not key: return {}
	else: return lkup(key)

def search(request):
	try:
		q = request.GET["q"]
	except KeyError:
		q = ""

	ctx = {"q": q,
		"articles": lookup(q)}
	return render(request, "search.html", ctx)
