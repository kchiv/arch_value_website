from rest_framework import serializers
from .models import Partner

class ListPartnerSerializer(serializers.ModelSerializer):
	partner_img = serializers.SerializerMethodField()

	def get_partner_img(self, obj):
		if obj.partner_logo:
			return obj.partner_logo.url
		else:
			return

	class Meta:
		model = Partner
		fields = ('id', 'partner_name', 'partner_listing_order', 'is_published', 'partner_img')
		depth = 1

class DetailPartnerSerializer(serializers.ModelSerializer):
	partner_img = serializers.SerializerMethodField()
	partner_website = serializers.SerializerMethodField()

	def get_partner_img(self, obj):
		if obj.partner_logo:
			return obj.partner_logo.url
		else:
			return

	def get_partner_website(self, obj):
		if obj.partner_url:
			return obj.partner_url
		else:
			return

	class Meta:
		model = Partner
		fields = ('id', 'partner_name', 'is_published', 'partner_img', 'partner_website', 'partner_description', 'partner_tag')
		depth = 1