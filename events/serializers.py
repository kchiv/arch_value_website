from rest_framework import serializers
from django_countries.serializers import CountryFieldMixin
from .models import Event

class EventSerializer(CountryFieldMixin, serializers.ModelSerializer):
	class Meta:
		model = Event
		fields = ('event_name',
				'is_published',
				'event_start',
				'event_end',
				'event_description',
				'event_country',
				'event_street',
				'event_city',
				'event_state',
				'event_partners')