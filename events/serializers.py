from rest_framework import serializers
from django_countries.serializers import CountryFieldMixin
from .models import Event
from partners.models import Partner

class PartnerNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ('id', 'partner_name', 'is_published')

class DetailEventSerializer(CountryFieldMixin, serializers.ModelSerializer):
	event_partners = PartnerNameSerializer(many=True)
	full_country_name = serializers.SerializerMethodField()
	full_description = serializers.SerializerMethodField()
	single_day_event = serializers.SerializerMethodField()
	start_date = serializers.SerializerMethodField()
	end_date = serializers.SerializerMethodField()
	year = serializers.SerializerMethodField()
	venue = serializers.SerializerMethodField()
	street = serializers.SerializerMethodField()
	city = serializers.SerializerMethodField()
	state = serializers.SerializerMethodField()
	feat_img = serializers.SerializerMethodField()

	def get_full_country_name(self, obj):
		return obj.event_country.name

	def get_full_description(self, obj):
		if obj.event_description == '':
			return None
		else:
			return obj.event_description

	def get_single_day_event(self, obj):
		if obj.event_start == obj.event_end:
			return True
		else:
			return False

	def get_start_date(self, obj):
		return obj.event_start.strftime('%b %d')

	def get_end_date(self, obj):
		return obj.event_end.strftime('%b %d')

	def get_year(self, obj):
		return obj.event_end.strftime('%Y')

	def get_venue(self, obj):
		if obj.event_venue == '':
			return None
		else:
			return obj.event_venue

	def get_street(self, obj):
		if obj.event_street == '':
			return None
		else:
			return obj.event_street

	def get_city(self, obj):
		if obj.event_city == '':
			return None
		else:
			return obj.event_city

	def get_state(self, obj):
		if obj.event_state == '':
			return None
		else:
			return obj.event_state

	def get_feat_img(self, obj):
		if obj.event_image:
			return obj.event_image.url
		else:
			return

	class Meta:
		model = Event
		fields = ('id', 
				'event_name', 
				'is_published',
				'feat_img', 
				'full_description', 
				'full_country_name', 
				'single_day_event', 
				'start_date', 
				'end_date', 
				'year', 
				'venue',
				'street',
				'city',
				'event_zip_code',
				'state',
				'event_partners')
		depth = 1

class ListEventSerializer(CountryFieldMixin, serializers.ModelSerializer):
	event_partners = PartnerNameSerializer(many=True)
	full_country_name = serializers.SerializerMethodField()
	single_day_event = serializers.SerializerMethodField()
	start_date = serializers.SerializerMethodField()
	end_date = serializers.SerializerMethodField()
	year = serializers.SerializerMethodField()
	venue = serializers.SerializerMethodField()
	street = serializers.SerializerMethodField()
	city = serializers.SerializerMethodField()
	state = serializers.SerializerMethodField()

	def get_full_country_name(self, obj):
		return obj.event_country.name

	def get_single_day_event(self, obj):
		if obj.event_start == obj.event_end:
			return True
		else:
			return False

	def get_start_date(self, obj):
		return obj.event_start.strftime('%b %d')

	def get_end_date(self, obj):
		return obj.event_end.strftime('%b %d')

	def get_year(self, obj):
		return obj.event_end.strftime('%Y')

	def get_venue(self, obj):
		if obj.event_venue == '':
			return None
		else:
			return obj.event_venue

	def get_street(self, obj):
		if obj.event_street == '':
			return None
		else:
			return obj.event_street

	def get_city(self, obj):
		if obj.event_city == '':
			return None
		else:
			return obj.event_city

	def get_state(self, obj):
		if obj.event_state == '':
			return None
		else:
			return obj.event_state

	class Meta:
		model = Event
		fields = ('id', 
				'event_name', 
				'is_published',
				'full_country_name', 
				'single_day_event', 
				'start_date', 
				'end_date', 
				'year', 
				'venue',
				'street',
				'city',
				'event_zip_code',
				'state',
				'event_partners')
		depth = 1