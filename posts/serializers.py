from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = ('author',
				'is_published',
				'meta_title',
				'header_title',
				'meta_description',
				'publication_date',
				'modification_date',
				'featured_image',
				'thumbnail_image',
				'post_content',
				'post_category',
				'post_tag',
				'post_slug')
		depth = 1