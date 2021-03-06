from django.shortcuts import render, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic.base import TemplateView
from .models import Post, Category, Tag
from rest_framework import generics
from .serializers import PostSerializer
from .pagination import StandardResultsPagination

# Create your views here.

class BlogHomePageView(TemplateView):

	template_name = 'posts/index.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['categories'] = Category.objects.all()
		return context

@staff_member_required
def post_preview(request, post_slug, post_id):
	post = get_object_or_404(Post, pk=post_id, post_slug=post_slug)

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

def tag_detail(request, tag_slug, tag_id):
	tag = get_object_or_404(Tag, pk=tag_id, tag_slug=tag_slug)

	context = {
		'tag': tag
	}
	return render(request, 'posts/tag_page.html', context)

class ListPostView(generics.ListAPIView):
	queryset = Post.objects.filter(is_published=True).order_by('-publication_date')
	serializer_class = PostSerializer
	pagination_class = StandardResultsPagination

class TagListPostView(generics.ListAPIView):
	serializer_class = PostSerializer
	pagination_class = StandardResultsPagination

	def get_queryset(self):
		tag_id = self.kwargs['tag_id']
		return Post.objects.filter(post_tag__pk=tag_id, is_published=True).order_by('-publication_date')

class CategoryPostListView(generics.ListAPIView):
	serializer_class = PostSerializer
	pagination_class = StandardResultsPagination

	def get_queryset(self):
		category_slug = self.kwargs['category_slug']
		return Post.objects.all().filter(post_category__category_slug=category_slug, is_published=True).order_by('-publication_date')