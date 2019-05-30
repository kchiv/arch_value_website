from django.db import models
from django.template.defaultfilters import slugify
from django.utils.html import strip_tags
from tinymce import HTMLField
from filebrowser.fields import FileBrowseField

# Create your models here.

class Page(models.Model):
	is_published = models.BooleanField(default=False, help_text='Check the box to publish page.')
	meta_title = models.CharField(max_length=100, unique=True, blank=False, help_text='Title that shows up in Google search.')
	header_title = models.CharField(max_length=100, unique=True, blank=True, help_text='Title that shows on page. Should typically match meta title.')
	meta_description = models.CharField(blank=True, max_length=250, help_text='Brief description that shows up in Google search. Approx. 160 characters.')
	featured_image = FileBrowseField('Featured image', max_length=500, extensions=['.jpg', 
																					'.jpeg', 
																					'.gif', 
																					'.png', 
																					'.tif', 
																					'.tiff'], blank=True, help_text='Image featured on page. Must be at least 1,000px X 1,000px')
	show_cta = models.BooleanField(default=False, help_text='Check the box to show CTA.')
	page_content = HTMLField('Content', blank=True)
	page_slug = models.SlugField(max_length=255, blank=True, unique=True, help_text='Text that shows in URL. Will automatically populate when object is saved.')
	custom_js = models.TextField(blank=True)
	custom_css = models.TextField(blank=True)

	def save(self, *args, **kwargs):
		if not self.page_slug:
			self.page_slug = slugify(self.meta_title)
		if not self.meta_description:
			self.meta_description = strip_tags(self.page_content[:230]) + '...'
		if not self.header_title:
			self.header_title = self.meta_title
		super(Page, self).save(*args, **kwargs)

	def __str__(self):
		return self.meta_title