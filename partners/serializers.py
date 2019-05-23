from rest_framework import serializers
from .models import Partner

class PartnerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Partner
		fields = ('partner_name',
				'is_published',
				'partner_logo',
				'partner_url',
				'partner_description',
				'partner_tag')