from django.db import models
from partners.models import Partner
from datetime import date
from localflavor.us.models import USStateField
from django_countries.fields import CountryField
from filebrowser.fields import FileBrowseField

# Create your models here.

class Event(models.Model):
	event_name = models.CharField(max_length=200)
	is_published = models.BooleanField(default=True, help_text='Check the box to publish event.')
	event_start = models.DateField(default=date.today)
	event_end = models.DateField(default=date.today)
	event_image = FileBrowseField('Event image', max_length=1000, extensions=['.jpg', 
														'.jpeg', 
														'.gif', 
														'.png', 
														'.tif', 
														'.tiff'], blank=True, null=True)
	event_description = models.TextField(blank=True, help_text='Brief description of event.')
	event_country = CountryField(blank=True, null=True, default='US')
	event_venue = models.CharField(max_length=300, blank=True)
	event_street = models.CharField(max_length=200, blank=True)
	event_city = models.CharField(max_length=100, blank=True)
	event_zip_code = models.IntegerField(blank=True, null=True)
	event_state = USStateField(null=True, blank=True, verbose_name='Event state (US only)')
	event_partners = models.ManyToManyField(Partner, blank=True)

	def __str__(self):
		return self.event_name