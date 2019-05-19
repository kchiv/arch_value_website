from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
from tinymce import HTMLField
from filebrowser.fields import FileBrowseField

# Create your models here.

class Category(models.Model):
	category_name = models.CharField(max_length=50, blank=False, unique=True)
	is_published = models.BooleanField(default=True)
	category_slug = models.SlugField(blank=True, unique=True)
	category_image = FileBrowseField('Category image', max_length=500, extensions=['.jpg', 
														'.jpeg', 
														'.gif', 
														'.png', 
														'.tif', 
														'.tiff'], blank=True)
	category_content = HTMLField('Category content', blank=True)

	class Meta:
		verbose_name_plural = 'categories'

	def save(self, *args, **kwargs):
		if not self.category_slug:
			self.category_slug = slugify(self.category_name)
		super(Category, self).save(*args, **kwargs)
	
	def __str__(self):
		return self.category_name

class Tag(models.Model):
	tag_name = models.CharField(max_length=50, blank=False, unique=True)
	tag_slug = models.SlugField(blank=True, unique=True)

	def save(self, *args, **kwargs):
		if not self.tag_slug:
			self.tag_slug = slugify(self.tag_name)
		super(Tag, self).save(*args, **kwargs)

	def __str__(self):
		return self.tag_name

class Post(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, models.SET_NULL, blank=True, null=True)
	is_published = models.BooleanField(default=True, help_text='Check the box to publish post.')
	meta_title = models.CharField(max_length=100, unique=True, blank=False, help_text='Title that shows up in Google search.')
	header_title = models.CharField(max_length=100, unique=True, help_text='Title that shows on page. Should typically match meta title.')
	post_slug = models.SlugField(blank=True, unique=True, help_text='Text that shows in URL.')
	meta_description = models.CharField(blank=True, max_length=250, help_text='Brief description that shows up in Google search. Approx. 160 characters.')
	publication_date = models.DateTimeField(help_text='Original publication date.')
	modification_date = models.DateTimeField(auto_now=True, help_text='Date the post was modified from original version.')
	featured_image = FileBrowseField('Featured image', max_length=500, extensions=['.jpg', 
																					'.jpeg', 
																					'.gif', 
																					'.png', 
																					'.tif', 
																					'.tiff'], blank=True, help_text='Image featured in post. Must be at least 1,000x1,000')
	thumbnail_image = FileBrowseField('Thumbnail image', max_length=500, extensions=['.jpg', 
																					'.jpeg', 
																					'.gif', 
																					'.png', 
																					'.tif', 
																					'.tiff'], blank=True, help_text='Thumbnail image used across site. Must be at least 1,000x1,000')
	post_content = HTMLField('Content', blank=True)
	post_category = models.ManyToManyField(Category)
	post_tag = models.ManyToManyField(Tag)

	def save(self, *args, **kwargs):
		if not self.post_slug:
			self.post_slug = slugify(self.meta_title)
		if not self.meta_description:
			self.meta_description = self.post_content[:230] + '...'
		if not self.header_title:
			self.header_title = self.meta_title
		super(Post, self).save(*args, **kwargs)

	def __str__(self):
		return self.meta_title