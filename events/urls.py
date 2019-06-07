from django.urls import path

from . import views

urlpatterns = [
	path('api/list-event/', views.ListEventView.as_view(), name='list_event'),
	path('api/event/<int:id>/', views.DetailEventView.as_view(), name='detail_event')
]