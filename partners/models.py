from django.db import models

# Create your models here.

class Partner(models.Model):
	partner_name = models.CharField(max_length=200)