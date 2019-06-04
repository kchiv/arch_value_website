from re import sub
from rest_framework import serializers
from django.urls import reverse
from django.utils.html import strip_tags
from django.contrib.auth.models import User
from .models import Post

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')

class PostSerializer(serializers.ModelSerializer):
	author = UserSerializer()
	post_title = serializers.SerializerMethodField()
	shorter_title = serializers.SerializerMethodField()
	strip_content = serializers.SerializerMethodField()
	shorter_content = serializers.SerializerMethodField()
	thumb_img = serializers.SerializerMethodField()
	feat_img = serializers.SerializerMethodField()
	post_url = serializers.SerializerMethodField()
	pub_date = serializers.SerializerMethodField()

	def get_post_title(self, obj):
		if len(obj.header_title) > 110:
			return obj.header_title[:110] + '...'
		else:
			return obj.header_title

	def get_shorter_title(self, obj):
		if len(obj.header_title) > 60:
			return obj.header_title[:60] + '...'
		else:
			return obj.header_title

	def get_strip_content(self, obj):
		remove_tags = strip_tags(obj.post_content)
		strip_newline = sub(r'\r\n', ' ', remove_tags)
		return strip_newline[:150] + '...'

	def get_shorter_content(self, obj):
		remove_tags = strip_tags(obj.post_content)
		strip_newline = sub(r'\r\n', ' ', remove_tags)
		return strip_newline[:90] + '...'

	def get_thumb_img(self, obj):
		return obj.thumbnail_image.url

	def get_feat_img(self, obj):
		return obj.featured_image.url

	def get_post_url(self, obj):
		return reverse('posts:post_detail', kwargs={'post_slug': obj.post_slug, 'post_id': obj.pk} )

	def get_pub_date(self, obj):
		return obj.publication_date.strftime('%b %d, %Y')

	class Meta:
		model = Post
		fields = ('id', 'author', 'is_published', 'pub_date', 'post_title', 'shorter_title', 'strip_content', 'shorter_content', 'post_category', 'thumb_img', 'feat_img', 'post_url')
		depth = 1