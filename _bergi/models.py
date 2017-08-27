from django.db import models

class Author(models.Model):
	slug = models.SlugField(max_length=31, unique=True)
	name = models.CharField(max_length=127)
	bio = models.CharField(max_length=1023)
	img = models.ImageField()

	def __str__(self):
		return self.name

class Cat(models.Model):
	slug = models.SlugField(max_length=31, unique=True)
	name = models.CharField(max_length=127)

	def __str__(self):
		return self.name

class Article(models.Model):
	authors = models.ManyToManyField(Author)
	cats = models.ManyToManyField(Cat)

	slug = models.SlugField(max_length=63, unique=True)
	title = models.CharField(max_length=255)
	content = models.TextField()
	img = models.ImageField()

	date = models.DateField()
	draft = models.BooleanField(default=True)
	pop = models.IntegerField(default=0)

	def __str__(self):
		return self.title
