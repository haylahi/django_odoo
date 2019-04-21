from rest_framework import generics

from . import models as m
from . import serializer as s


class BrandCreateListView(generics.ListCreateAPIView):
    queryset = m.ProductBrand.objects.filter(is_active=True)
    serializer_class = s.BrandSerializer


class CategoryCreateListView(generics.ListCreateAPIView):
    queryset = m.ProductCategory.objects.filter(is_active=True)
    serializer_class = s.CategorySerializer


class ProductCreateListView(generics.ListCreateAPIView):
    queryset = m.ProductProduct.objects.filter(is_active=True)
    serializer_class = s.ProductSerializer


class ProductPriceListCreateListView(generics.ListCreateAPIView):
    queryset = m.ProductPriceList.objects.filter(is_active=True)
    serializer_class = s.ProductPriceListSerializer


class ProductPriceItemCreateListView(generics.ListCreateAPIView):
    queryset = m.ProductPriceItem.objects.filter(is_active=True)
    serializer_class = s.ProductPriceItemSerializer


# -----------------------------------------------------------------------------


class AppearanceTypeCreateListView(generics.ListCreateAPIView):
    queryset = m.AppearanceType.objects.filter(is_active=True)
    serializer_class = s.AppearanceTypeSerializer


class AppearanceGroupListCreateView(generics.ListCreateAPIView):
    queryset = m.AppearanceGroup.objects.filter(is_active=True)
    serializer_class = s.AppearanceGroupSerializer


class AppearanceItemCreateListView(generics.ListCreateAPIView):
    queryset = m.AppearanceItem.objects.filter(is_active=True)
    serializer_class = s.AppearanceItemSerializer
