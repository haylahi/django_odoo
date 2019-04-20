# author: Liberty
# date: 2019/4/20 22:47

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index_page, name='index'),
    url(r'^(?P<room_name>[^/]+)/$', views.room_page, name='room'),
]
