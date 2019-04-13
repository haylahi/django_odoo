# author: Liberty
# date: 2019/4/13 16:49

from django.urls import path

from .views import UserRegisterView, BaseCountryView, CountryDetailView

urlpatterns = [
    path('user/', UserRegisterView.as_view()),
    path('country/', BaseCountryView.as_view()),
    path('country/<int:pk>/', CountryDetailView.as_view()),
]
