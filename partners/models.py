from django.db import models
from tinymce import HTMLField
from filebrowser.fields import FileBrowseField

# Create your models here.

class Partner(models.Model):
	partner_name = models.CharField(max_length=200)
	partner_logo = FileBrowseField('Partner logo', max_length=1000, extensions=['.jpg', 
														'.jpeg', 
														'.gif', 
														'.png', 
														'.tif', 
														'.tiff'], blank=True)
	partner_description = HTMLField('Partner description', blank=True)

	def __str__(self):
		return self.partner_name