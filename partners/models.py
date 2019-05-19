from django.db import models
from posts.models import Tag
from tinymce import HTMLField
from filebrowser.fields import FileBrowseField

# Create your models here.

class Partner(models.Model):
	partner_name = models.CharField(max_length=200)
	is_published = models.BooleanField(default=True, help_text='Check the box to publish Partner.')
	partner_logo = FileBrowseField('Partner logo', max_length=1000, extensions=['.jpg', 
														'.jpeg', 
														'.gif', 
														'.png', 
														'.tif', 
														'.tiff'], blank=True)
	partner_url = models.URLField(blank=True, help_text='Enter the URL for partner website.')
	partner_description = HTMLField('Partner description', blank=True)
	partner_tag = models.ForeignKey(Tag, models.SET_NULL, blank=True, null=True, help_text='Select tag for the partner if it exists. This will populate blog posts with that tag.')

	def __str__(self):
		return self.partner_name