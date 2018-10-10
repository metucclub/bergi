from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.template.defaultfilters import slugify

from django.db.models import Q, Count
from django.core.paginator import *
from django.conf import settings

from .models import *
from .search import recommends

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
	return render(request, "_bergi/index.html", ctx)

def author(request, slug):
	author = get_object_or_404(Author, slug=slug)
	ctx = {"author": author,
		"author_articles": author.articles.exclude(draft=True),
		"title": author.name}
	return render(request, "_bergi/author.html", ctx)

# XXX: currently people can take peeks at draft articles if they know the link.
# fix is trivial(s/Article/Article.nondraft) but current state is useful for a preview-ish.
def article(request, slug):
	article = get_object_or_404(Article, slug=slug)

	ctx = {"article": article,
		"recommends": recommends(article),
		"title": article.title}
	return render(request, "_bergi/article.html", ctx)

# we have legacy articles with non-conforming slugs.
# tame them by redirecting permanently.
def irregular_article(request, raw_slug):
	slug = slugify(raw_slug)
	return redirect("article", slug, permanent=True)

# generic fn to use with paginated views.
# returns a context with the Page obj,
# a range for templates/_bergi/_paginator.html and whether to show ellipses(…).
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

# XXX: it's blinking at you
def archive(request, page):
	paginator = Paginator(Article.nondraft.all()[13:], per_page=settings.PER_PAGE, orphans=settings.ORPHANS)

	ctx = page_ctx(paginator, page)
	ctx["title"] = "Arşiv"

	return render(request, "_bergi/archive.html", ctx)

def cat(request, slug, page):
	cat = get_object_or_404(Cat, slug=slug)
	paginator = Paginator(cat.articles.exclude(draft=True), per_page=settings.PER_PAGE, orphans=settings.ORPHANS)

	ctx = page_ctx(paginator, page)
	ctx["cat"] = cat
	ctx["title"] = cat.name

	return render(request, "_bergi/cat.html", ctx)

from .search import search as S
def search(request):
	try:
		q = request.GET["q"]
	except KeyError:
		q = ""

	ctx = {"q": q, "articles": S(q), "title": q}
	return render(request, "_bergi/search.html", ctx)

def about(request):
	ctx = {"title": "Hakkında"}
	return render(request, "_bergi/about.html", ctx)

# XXX: also counts draft articles.
def team(request):
	ctx = {"staples": Author.objects.annotate(x=Count("articles")).filter(x__gte=5),
		"title": "Künye"}
	return render(request, "_bergi/team.html", ctx)
