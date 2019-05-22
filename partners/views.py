from django.shortcuts import render, get_object_or_404
from .models import Partner
from rest_framework import generics
from .serializers import PartnerSerializer

# Create your views here.

def index(request):
	return render(request, 'events/event_page.html')

class ListPartnerView(generics.ListAPIView):
	queryset = Partner.objects.all()
	serializer_class = PartnerSerializer