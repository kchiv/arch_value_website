from .models import Event
from rest_framework import generics
from .serializers import EventSerializer

# Create your views here.

class ListEventView(generics.ListAPIView):
	queryset = Event.objects.all()
	serializer_class = EventSerializer