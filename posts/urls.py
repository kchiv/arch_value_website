from django.urls import path

from . import views

urlpatterns = [
	path('preview/<int:post_id>', views.post_preview, name='post_preview'),
	path('<slug:post_slug>/<int:post_id>', views.post_detail, name='post_detail'),
]