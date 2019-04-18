import random

from django.http import HttpResponse
from rest_framework import generics

from base.serializer import CountrySerializer, ProvinceSerializer, CitySerializer
from .models import BaseCountry, BaseProvince, BaseCity

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


# -----------------------------------------------------------------------------


def test_test(request):
    from .tasks import task_test
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    ret = 'null'
    try:
        task = task_test.delay(a, b)
        ret = task.get(timeout=1)
    except:
        _log.error('任务执行失败')
    return HttpResponse('<h2>200 OK</h2> {ret}'.format(ret=ret), content_type='text/html; charset=utf-8', status=200)
