# author: Liberty
# date: 2019/4/14 20:48

from django.urls import path

from . import views as _v

urlpatterns = [
    path('warehouse/', _v.StockWarehouseListCreateView.as_view()),
    path('location/', _v.LocationListCreateView.as_view()),
    path('stock_picking_type/', _v.StockPickingTypeListCreateView.as_view()),
]
