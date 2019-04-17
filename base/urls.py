# author: Liberty
# date: 2019/4/13 16:49
from django.urls import path

from .views import CountryListCreateView, test_test, CountryDetailUpdateView

urlpatterns = [
    path('country/', CountryListCreateView.as_view()),
    path('country/<int:pk>/', CountryDetailUpdateView.as_view()),
    path('test/', test_test)
]
