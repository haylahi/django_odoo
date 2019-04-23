# author: Liberty
# date: 2019/4/22 20:50

from django.urls import path

from base import views

urlpatterns = [
    path('unit/', views.UnitCreateListView.as_view({'get': 'show_unit_list', 'post': 'create_unit'})),

    path('test/', views.base_test),
]
