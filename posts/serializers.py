from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')

class PostSerializer(serializers.ModelSerializer):
	author = UserSerializer()
	class Meta:
		model = Post
		fields = '__all__'
		depth = 1