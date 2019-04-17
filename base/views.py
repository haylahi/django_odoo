from django.http import HttpResponse
from rest_framework import generics

from base.serializer import CountrySerializer, ProvinceSerializer, CitySerializer
from .models import BaseCountry, BaseProvince, BaseCity


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


# -----------------------------------------------------------------------------


def test_test(request):
    from .tasks import task_test
    try:
        r = task_test.delay(1, 2)
        print(r.get(timeout=1))
    except Exception:
        pass
    return HttpResponse('<h2>200 OK</h2> ', content_type='text/html; charset=utf-8', status=200)
