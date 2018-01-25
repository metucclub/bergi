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
	on_navbar = models.BooleanField(default=False)

	def __str__(self):
		return self.name

# so we don't .exclude(draft=True) everywhere on views.py.
# XXX: maybe make this the default manager? currently everything in views.py uses this.
class NondraftManager(models.Manager):
	use_for_related_fields = True
	def get_queryset(self):
		return super().get_queryset().exclude(draft=True)

class Article(models.Model):
	authors = models.ManyToManyField(Author, related_name="articles")
	cats = models.ManyToManyField(Cat, related_name="articles")

	slug = models.SlugField(max_length=63, unique=True)
	title = models.CharField(max_length=255)
	content = models.TextField()
	img = models.ImageField()

	date = models.DateField()
	draft = models.BooleanField(default=True)
	pop = models.IntegerField(default=0)

	objects = models.Manager()
	nondraft = NondraftManager()

	class Meta:
		ordering = ["-date"]

	def __str__(self):
		return self.title
