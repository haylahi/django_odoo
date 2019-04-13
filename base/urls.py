# author: Liberty
# date: 2019/4/13 16:49

from django.urls import path

from .views import UserRegisterView, BaseCountryListView, CountryDetailView, \
    ProvinceListView, ProvinceDetailView, UnitListView

urlpatterns = [
    path('user/', UserRegisterView.as_view()),
    path('country/', BaseCountryListView.as_view()),
    path('country/<int:pk>/', CountryDetailView.as_view()),
    path('province/', ProvinceListView.as_view()),
    path('province/<int:pk>/', ProvinceDetailView.as_view()),
    path('baseunit/', UnitListView.as_view())
]
