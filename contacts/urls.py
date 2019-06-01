from django.urls import path

from . import views

app_name = 'contacts'

urlpatterns = [
	path('hp-contact/', views.hp_contact_form, name='hp_contact')
]