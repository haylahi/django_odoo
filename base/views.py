import random

from django.http import HttpResponse
from rest_framework import generics

from base.serializer import CountrySerializer, ProvinceSerializer, CitySerializer, UnitSerializer
from .models import BaseCountry, BaseProvince, BaseCity, BaseUnit

import logging

_log = logging.getLogger(__name__)


class CountryListCreateView(generics.ListCreateAPIView):
    queryset = BaseCountry.objects.filter(is_active=True)
    serializer_class = CountrySerializer


class CountryDetailUpdateView(generics.RetrieveUpdateAPIView):
    queryset = BaseCountry.objects.filter(is_active=True)
    serializer_class = CountrySerializer


class ProvinceListCreateView(generics.ListCreateAPIView):
    queryset = BaseProvince.objects.filter(is_active=True)
    serializer_class = ProvinceSerializer


class CityListCreateView(generics.ListCreateAPIView):
    queryset = BaseCity.objects.filter(is_active=True)
    serializer_class = CitySerializer


class UnitListCreateView(generics.ListCreateAPIView):
    queryset = BaseUnit.objects.filter(is_active=True)
    serializer_class = UnitSerializer


# -----------------------------------------------------------------------------


def test_test(request):
    ret = 'null'
    return HttpResponse('<h2>200 OK</h2> <h3>{ret}</h3>'.format(ret=ret), content_type='text/html; charset=utf-8', status=200)
