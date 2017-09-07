from django.shortcuts import render
from django.http import HttpResponse

from .models import *

ctx = {"cats": Cat.objects.all()}

def index(request):
	ctx = {"articles": Article.objects.order_by("-date"),
		"articles_pop": Article.objects.order_by("pop")}
	return render(request, "index.html", ctx)

def author(request, slug):
	ctx = {"author": Author.objects.get(slug=slug)}
	return render(request, "author.html", ctx)

def article(request, slug):
	ctx = {"article": Article.objects.get(slug=slug)}
	return render(request, "article.html", ctx)

def cat(request, slug):
	ctx = {"cat": Cat.objects.get(slug=slug)}
	return render(request, "cat.html", ctx)
