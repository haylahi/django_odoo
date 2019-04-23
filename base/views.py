# author: Liberty
# date: 2019/4/22 20:51
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response

from . import models
from . import serializer as s


class UnitCreateListView(viewsets.ViewSet):
    def show_unit_list(self, request, *args, **kwargs):
        result = models.BaseUnit.objects.filter(is_active=True)
        serializer = s.BaseUnitSerializer(result, many=True)
        return Response(serializer.data)


def base_test(request):
    return HttpResponse('<h2>200 OK</h2>', content_type='text/html', status=200)
