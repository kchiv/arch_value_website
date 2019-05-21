from django.shortcuts import render, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required

from .models import Post

# Create your views here.

@staff_member_required
def post_preview(request, post_id):
	post = get_object_or_404(Post, pk=post_id)

	context = {
		'post': post
	}
	return render(request, 'posts/post_preview.html', context)