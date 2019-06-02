from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
	path('', views.BlogHomePageView.as_view(), name='index'),
	path('preview/<slug:post_slug>/<int:post_id>/', views.post_preview, name='post_preview'),
	path('<slug:post_slug>/<int:post_id>/', views.post_detail, name='post_detail'),
	path('api/list-post/', views.ListPostView.as_view(), name='list_post'),
	path('api/<slug:category_slug>/', views.CategoryPostListView.as_view(), name='category_list_post')
]