from django.db import models
from django.conf import settings
from tinymce import HTMLField
from filebrowser.fields import FileBrowseField

# Create your models here.

class Category(models.Model):
	category_name = models.CharField(max_length=200)
	is_published = models.BooleanField(default=True)
	category_slug = models.SlugField(unique=True)
	category_image = FileBrowseField('Category image', max_length=1000, extensions=['.jpg', 
														'.jpeg', 
														'.gif', 
														'.png', 
														'.tif', 
														'.tiff'], blank=True)
	category_content = HTMLField('Category content', blank=True)


	def __str__(self):
		return self.category_name

class Tag(models.Model):
	tag_name = models.CharField(max_length=300)
	tag_slug = models.SlugField(unique=True)

	def __str__(self):
		return self.tag_name

class Post(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, models.SET_NULL, blank=True, null=True)
	is_published = models.BooleanField(default=True)
	title = models.CharField(max_length=700)
	post_slug = models.SlugField(unique=True)
	publication_date = models.DateTimeField(auto_now_add=True)
	featured_image = FileBrowseField('Featured image', max_length=1000, extensions=['.jpg', 
														'.jpeg', 
														'.gif', 
														'.png', 
														'.tif', 
														'.tiff'], blank=True)
	post_content = HTMLField('Content', blank=True)
	post_category = models.ManyToManyField(Category)
	post_tag = models.ManyToManyField(Tag)


	def __str__(self):
		return self.title