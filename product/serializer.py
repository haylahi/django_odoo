# author: Liberty
# date: 2019/4/21 15:36

from rest_framework import serializers

from . import models as m

"""
code 唯一性验证

"""


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.ProductBrand
        fields = '__all__'
        read_only_fields = ('create_time', 'is_active')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = m.ProductCategory
        fields = '__all__'
        read_only_fields = ('create_time', 'is_active')
