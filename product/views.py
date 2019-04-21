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
