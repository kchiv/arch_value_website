from rest_framework import serializers
from django_countries.serializers import CountryFieldMixin
from .models import Event

class EventSerializer(CountryFieldMixin, serializers.ModelSerializer):

	class Meta:
		model = Event
		fields = '__all__'
		depth = 1