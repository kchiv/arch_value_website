from django.urls import path

from . import views

urlpatterns = [
	path('preview/<int:page_id>', views.page_preview, name='page_preview'),
	path('<slug:page_slug>', views.page_detail, name='page_detail')
]