from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
	path('', views.BlogHomePageView.as_view(), name='index'),
	path('preview/<slug:post_slug>/<int:post_id>/', views.post_preview, name='post_preview'),
	path('<slug:post_slug>/<int:post_id>/', views.post_detail, name='post_detail'),
	path('tag/<slug:tag_slug>/<int:tag_id>/', views.tag_detail, name='tag_detail'),
	path('api/list-post/', views.ListPostView.as_view(), name='list_post'),
	path('api/category/<slug:category_slug>/', views.CategoryPostListView.as_view(), name='category_list_post'),
	path('api/tag/<int:tag_id>/', views.TagListPostView.as_view(), name='tag_list_post')
]