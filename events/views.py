from django.shortcuts import render, get_object_or_404
from .models import Event
from rest_framework import generics
from .serializers import EventSerializer

# Create your views here.

def index(request):
	return render(request, 'events/event_page.html')

class ListEventView(generics.ListAPIView):
	queryset = Event.objects.all()
	serializer_class = EventSerializer