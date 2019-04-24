# author: Liberty
# date: 2019/4/22 20:51
from django.http import HttpResponse
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from . import models
from . import serializer as s


class UnitCreateListView(viewsets.ViewSet):
    def show_unit_list(self, request, *args, **kwargs):
        # TODO 分页
        result = models.BaseUnit.objects.filter(is_active=True)
        serializer = s.BaseUnitSerializer(result, many=True)
        return Response(serializer.data)

    def create_unit(self, request, *args, **kwargs):
        serializer = s.BaseUnitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def base_test(request):
    # import random
    # User = models.BaseUser
    #
    # username = str(random.randint(1, 10000))
    # User.objects.create(username=username)

    return HttpResponse('<h2>200 OK</h2>', content_type='text/html', status=200)
