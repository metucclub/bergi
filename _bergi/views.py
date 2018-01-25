from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.template.defaultfilters import slugify

from django.db.models import Q, Count
from django.core.paginator import *
from django.conf import settings

from .models import *

import random

# We need this to put "cats" in global context, so every view doesn't have to call Cat.objects.get for the navigation bar.
# See how it is pipelined in ../bergi/settings/base.py:/context_processors/ .
def cats_on_navbar(request):
	return {"cats": Cat.objects.filter(on_navbar=True).order_by("slug")}

# get_object_or_404 looks like a custom function, but it is a Django shortcut.
# we don't place any post in Pop if it's already on the page.
# XXX: magic numbers all over the place
def index(request):
	articles = list(Article.nondraft.all()[:13])
	cover = articles[:3]
	river = articles[3:13]
	pop = Article.nondraft.exclude(pk__in=([o.pk for o in cover]+[o.pk for o in river])).order_by("-pop")[:4]
	ctx = {"cover": cover, "river": river, "pop": pop}
	return render(request, "index.html", ctx)

def author(request, slug):
	author = get_object_or_404(Author, slug=slug)
	ctx = {"author": author,
		"author_articles": author.articles.exclude(draft=True),
		"title": author.name}
	return render(request, "author.html", ctx)

# current recommendation algorithm is ducktape and close to random:
# mix 4 popular articles and articles with same cat or author, draw 4.
# XXX: currently people can take peeks at draft articles if they know the link.
# fix is trivial(s/Article/Article.nondraft) but current state is useful for a preview-ish.
def article(request, slug):
	article = get_object_or_404(Article, slug=slug)
	other_articles = Article.nondraft.exclude(slug=slug)

	# see https://stackoverflow.com/questions/739776
	r = other_articles.filter(Q(cats__in=article.cats.all()) | Q(authors__in=article.authors.all())) | other_articles.order_by("pop")[:4]
	r = list(r.distinct())
	random.shuffle(r)
	recommends = r[:4]

	ctx = {"article": article,
		"recommends": recommends,
		"title": article.title}
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
# XXX: it's blinking at you
def archive(request, page):
	paginator = Paginator(Article.nondraft.all()[13:], per_page=settings.PER_PAGE, orphans=settings.ORPHANS)

	ctx = page_ctx(paginator, page)
	ctx["title"] = "Arşiv"

	return render(request, "archive.html", ctx)

def cat(request, slug, page):
	cat = get_object_or_404(Cat, slug=slug)
	paginator = Paginator(cat.articles.exclude(draft=True), per_page=settings.PER_PAGE, orphans=settings.ORPHANS)

	ctx = page_ctx(paginator, page)
	ctx["cat"] = cat
	ctx["title"] = cat.name

	return render(request, "cat.html", ctx)

# __search is a Postgres feature.
# XXX: remove magic number 10
from django.db import connection
if connection.vendor == "postgresql":
        from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
        def lkup(key):
                query = SearchQuery(key, config="turkish")
                vec = SearchVector("content", config="turkish")
                rank = SearchRank(vec, query)
                final = Article.nondraft.annotate(search=vec, rank=rank).filter(search=query).order_by("-rank")[:10]
                return final

# just icontains on sqlite
else:
	def lkup(key):
		return Article.nondraft.filter(content__icontains=key)[:10]

def lookup(key):
	if not key: return {}
	else: return lkup(key)

def search(request):
	try:
		q = request.GET["q"]
	except KeyError:
		q = ""

	ctx = {"q": q,
		"articles": lookup(q),
		"title": q}
	return render(request, "search.html", ctx)

def about(request):
	ctx = {"title": "Hakkında"}
	return render(request, "about.html", ctx)

# XXX: also counts draft articles.
def team(request):
	ctx = {"staples": Author.objects.annotate(x=Count("article")).filter(x__gte=5),
		"title": "Künye"}
	return render(request, "team.html", ctx)
