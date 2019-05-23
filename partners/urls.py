from django.urls import path

from . import views

urlpatterns = [
	path('api/list-partner', views.ListPartnerView.as_view(), name='list_partner')
]