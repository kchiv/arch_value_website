from .models import Partner
from rest_framework import generics
from .serializers import PartnerSerializer

# Create your views here.

class ListPartnerView(generics.ListAPIView):
	queryset = Partner.objects.all()
	serializer_class = PartnerSerializer