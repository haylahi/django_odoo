# author: Liberty
# date: 2019/4/21 15:37

from django.urls import path

from . import views as v

urlpatterns = [
    path('brand/', v.BrandCreateListView.as_view()),
]
