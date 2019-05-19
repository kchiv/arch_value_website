from django.db import models
from partners.models import Partner
from datetime import date
from localflavor.us.models import USStateField

# Create your models here.

class Event(models.Model):
	event_name = models.CharField(max_length=200)
	is_published = models.BooleanField(default=True, help_text='Check the box to publish event.')
	event_start = models.DateField(default=date.today)
	event_end = models.DateField(default=date.today)
	event_street = models.CharField(max_length=200, blank=True)
	event_city = models.CharField(max_length=100, blank=True)
	event_state = USStateField(blank=True)
	event_partners = models.ManyToManyField(Partner, blank=True)

	def __str__(self):
		return self.event_name