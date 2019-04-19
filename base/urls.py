# author: Liberty
# date: 2019/4/13 16:49
from django.urls import path

from .views import (
    test_test,
    CountryListCreateView, CountryDetailUpdateView,
    ProvinceListCreateView, CityListCreateView, UnitListCreateView,
    CurrencyListCreateView, CurrencyRateListCreateView,
    TaxListCreateView, CompanyListCreateView
)

urlpatterns = [
    path('country/', CountryListCreateView.as_view()),
    path('country/<int:pk>/', CountryDetailUpdateView.as_view()),
    path('province/', ProvinceListCreateView.as_view()),
    path('city/', CityListCreateView.as_view()),
    path('currency/', CurrencyListCreateView.as_view()),
    path('currency_rate/', CurrencyRateListCreateView.as_view()),
    path('unit/', UnitListCreateView.as_view()),
    path('tax/', TaxListCreateView.as_view()),

    path('company/', CompanyListCreateView.as_view()),

    # ----------------------------------------------------------
    path('test/', test_test)
]
