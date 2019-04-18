import logging

from django.http import HttpResponse
from rest_framework import generics

from base.serializer import (
    CountrySerializer, ProvinceSerializer, CitySerializer,
    UnitSerializer, CurrencySerializer, CurrencyRateSerializer,
    TaxSerializer
)
from .models import (
    BaseCountry, BaseProvince, BaseCity,
    BaseUnit, Currency, CurrencyRate,
    BaseTax
)

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


class CurrencyListCreateView(generics.ListCreateAPIView):
    queryset = Currency.objects.filter(is_active=True)
    serializer_class = CurrencySerializer


class CurrencyRateListCreateView(generics.ListCreateAPIView):
    queryset = CurrencyRate.objects.filter(is_active=True)
    serializer_class = CurrencyRateSerializer


class TaxListCreateView(generics.ListCreateAPIView):
    queryset = BaseTax.objects.filter(is_active=True)
    serializer_class = TaxSerializer


# -----------------------------------------------------------------------------


def test_test(request):
    return HttpResponse('<h2>200 OK</h2> <h3></h3>', content_type='text/html; charset=utf-8', status=200)
