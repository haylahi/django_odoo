# author: Liberty
# date: 2019/4/22 20:50

from django.urls import path
from base import views

urlpatterns = [
    path('test/', views.base_test),
]
