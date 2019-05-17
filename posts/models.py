from django.db import models
from tinymce import HTMLField

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=1000)
	content = HTMLField('Content')


	def __str__(self):
		return self.title