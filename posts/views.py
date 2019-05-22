from django.shortcuts import render, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from .models import Post
from rest_framework import generics
from .serializers import PostSerializer

# Create your views here.

@staff_member_required
def post_preview(request, post_id):
	post = get_object_or_404(Post, pk=post_id)

	context = {
		'post': post
	}
	return render(request, 'posts/post_page.html', context)

def post_detail(request, post_slug, post_id):
	post = get_object_or_404(Post, pk=post_id, post_slug=post_slug)

	context = {
		'post': post
	}
	return render(request, 'posts/post_page.html', context)

class ListPostView(generics.ListAPIView):
	queryset = Post.objects.all().order_by('-publication_date')
	serializer_class = PostSerializer