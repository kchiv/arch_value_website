from django.urls import path

from . import views

app_name = 'pages'

urlpatterns = [
	path('preview/<slug:page_slug>/', views.page_preview, name='page_preview'),
	path('<slug:page_slug>/', views.page_detail, name='page_detail')
]