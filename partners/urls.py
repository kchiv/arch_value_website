from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('api/list-partner', views.ListPartnerView.as_view(), name='list_partner')
]