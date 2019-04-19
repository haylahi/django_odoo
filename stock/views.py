from rest_framework import generics

from . import models as _m
from . import serializer as _s


class StockWarehouseListCreateView(generics.ListCreateAPIView):
    queryset = _m.StockWarehouse.objects.filter(is_active=True)
    serializer_class = _s.StockWarehouseSerializer


class LocationListCreateView(generics.ListCreateAPIView):
    queryset = _m.StockLocation.objects.filter(is_active=True)
    serializer_class = _s.LocationSerializer
