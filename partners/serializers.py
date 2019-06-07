from rest_framework import serializers
from .models import Partner

class ListPartnerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Partner
		fields = '__all__'
		depth = 1

class DetailPartnerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Partner
		fields = '__all__'
		depth = 1