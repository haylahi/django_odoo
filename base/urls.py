# author: Liberty
# date: 2019/4/13 16:49

from django.urls import path

from .views import UserRegisterView, BaseCountryListView, CountryDetailView, \
    ProvinceListView, ProvinceDetailView, UnitListView, test_function_view, \
    CompanyListView, TaxListView, CurrencyListView, CurrencyRateListView

urlpatterns = [
    path('test/', test_function_view),
    path('user/', UserRegisterView.as_view()),
    path('country/', BaseCountryListView.as_view()),
    path('country/<int:pk>/', CountryDetailView.as_view()),
    path('province/', ProvinceListView.as_view()),
    path('province/<int:pk>/', ProvinceDetailView.as_view()),
    path('unit/', UnitListView.as_view()),
    path('company/', CompanyListView.as_view()),
    path('tax/', TaxListView.as_view()),
    path('currency/', CurrencyListView.as_view()),
    path('currencyrate/', CurrencyRateListView.as_view())
]
