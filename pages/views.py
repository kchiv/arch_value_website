from django.shortcuts import render, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from .models import Page

# Create your views here.

@staff_member_required
def page_preview(request, page_id):
	page = get_object_or_404(Page, pk=page_id)

	context = {
		'page': page
	}
	return render(request, 'pages/page_detail.html', context)

def page_detail(request, page_slug):
	page = get_object_or_404(Page, page_slug=page_slug)

	context = {
		'page': page
	}
	return render(request, 'pages/page_detail.html', context)