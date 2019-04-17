from django.http import HttpResponse
from rest_framework import generics

from base.serializer import CountrySerializer
from .models import BaseCountry


class CountryListCreateView(generics.ListCreateAPIView):
    queryset = BaseCountry.objects.filter(is_active=True)
    serializer_class = CountrySerializer


class CountryDetailUpdateView(generics.RetrieveUpdateAPIView):
    queryset = BaseCountry.objects.filter(is_active=True)
    serializer_class = CountrySerializer


# -----------------------------------------------------------------------------


def test_test(request):
    return HttpResponse('<h2>200 OK</h2> ', content_type='text/html; charset=utf-8', status=200)
