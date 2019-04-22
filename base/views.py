# author: Liberty
# date: 2019/4/22 20:51
from django.http import HttpResponse

from rest_framework import viewsets


class ProvinceListCreate(viewsets.ViewSet):
    """省份的创建和展示"""


def base_test(request):
    return HttpResponse('<h2>200 OK</h2>', content_type='text/html', status=200)
