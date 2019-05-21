from django.urls import path

from . import views

urlpatterns = [
	path('preview/<int:post_id>', views.post_preview, name='post_preview')
]