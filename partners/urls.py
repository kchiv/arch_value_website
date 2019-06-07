from django.urls import path

from . import views

urlpatterns = [
	path('api/list-partner/', views.ListPartnerView.as_view(), name='list_partner'),
	path('api/partner/<int:id>', views.DetailPartnerView.as_view(), name='detail_partner')
]