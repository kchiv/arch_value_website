from django.db import models
from datetime import date

# Create your models here.

class Event(models.Model):
	event_name = models.CharField(max_length=200)
	event_start = models.DateField(default=date.today)
	event_end = models.DateField(default=date.today)
	event_address = models.CharField(max_length=500)

	def __str__(self):
		return self.event_name