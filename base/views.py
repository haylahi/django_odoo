# author: Liberty
# date: 2019/4/22 20:51
from django.http import HttpResponse


def base_test(request):
    return HttpResponse('<h2>200 OK</h2>', content_type='text/html', status=200)
