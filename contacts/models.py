from django.db import models

# Create your models here.

class Contact(models.Model):
	user_type = models.CharField(max_length=20, blank=True)
	name = models.CharField(max_length=50, blank=True)
	email = models.EmailField(blank=True)
	phone_number = models.CharField(max_length=50, blank=True)
	company_name = models.CharField(max_length=100, blank=True)
	message = models.CharField(max_length=1000, blank=True)
	subscriber = models.BooleanField(default=False)
	contact_date = models.DateTimeField(auto_now_add=True, blank=True)

	def __str__(self):
		return self.name