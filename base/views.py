from rest_framework import generics

from base.serializer import CountrySerializer
from .models import BaseCountry


class CountryListCreateView(generics.ListCreateAPIView):
    queryset = BaseCountry.objects.filter(is_active=True)
    serializer_class = CountrySerializer
