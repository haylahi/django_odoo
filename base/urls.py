# author: Liberty
# date: 2019/4/13 16:49

from django.urls import path

from .views import UserRegisterView

urlpatterns = [
    path('user/', UserRegisterView.as_view()),
]