from datetime import datetime
from .models import Event
from rest_framework import generics
from .serializers import DetailEventSerializer, ListEventSerializer
from .pagination import EventsResultsPagination

# Create your views here.

class ListEventView(generics.ListAPIView):
	current_date = datetime.now().date()
	queryset = Event.objects.filter(is_published=True, event_end__gte=current_date).order_by('-event_end')
	serializer_class = ListEventSerializer
	pagination_class = EventsResultsPagination

class DetailEventView(generics.RetrieveAPIView):
	lookup_field = 'id'
	queryset = Event.objects.all()
	serializer_class = DetailEventSerializer