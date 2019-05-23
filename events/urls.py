from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('api/list-event', views.ListEventView.as_view(), name='list_event')
]