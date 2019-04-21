# author: Liberty
# date: 2019/4/21 15:36

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from . import models as m

"""
code 唯一性验证

"""


class BrandSerializer(serializers.ModelSerializer):
    code = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=m.ProductBrand.objects.filter(is_active=True))]
    )

    class Meta:
        model = m.ProductBrand
        fields = '__all__'
        read_only_fields = ('create_time', 'is_active')


class CategorySerializer(serializers.ModelSerializer):
    code = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=m.ProductCategory.objects.filter(is_active=True))]
    )

    class Meta:
        model = m.ProductCategory
        fields = '__all__'
        read_only_fields = ('create_time', 'is_active')


class ProductSerializer(serializers.ModelSerializer):
    code = serializers.CharField(
        required=True, label='编码',
        validators=[UniqueValidator(queryset=m.ProductProduct.objects.filter(is_active=True))]
    )

    class Meta:
        model = m.ProductProduct
        fields = '__all__'
        read_only_fields = ('create_time', 'is_active')
