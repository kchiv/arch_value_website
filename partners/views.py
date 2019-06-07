from .models import Partner
from rest_framework import generics
from .serializers import ListPartnerSerializer, DetailPartnerSerializer
from .pagination import PartnersResultsPagination

# Create your views here.

class ListPartnerView(generics.ListAPIView):
	queryset = Partner.objects.filter(is_published=True).order_by('partner_listing_order')
	serializer_class = ListPartnerSerializer
	pagination_class = PartnersResultsPagination

class DetailPartnerView(generics.RetrieveAPIView):
	lookup_field = 'id'
	queryset = Partner.objects.all()
	serializer_class = DetailPartnerSerializer