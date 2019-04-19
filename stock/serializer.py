# author: Liberty
# date: 2019/4/14 20:48

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from . import models as _m


class StockWarehouseSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        label='仓库名称',
        validators=[UniqueValidator(queryset=_m.StockWarehouse.objects.filter(is_active=True))]
    )
    code = serializers.CharField(
        label='仓库编号',
        validators=[UniqueValidator(queryset=_m.StockWarehouse.objects.filter(is_active=True))]
    )

    class Meta:
        model = _m.StockWarehouse
        fields = '__all__'
        read_only_fields = ('create_time', 'is_active')


class LocationSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        label='位置名称',
        validators=[UniqueValidator(queryset=_m.StockWarehouse.objects.filter(is_active=True))]
    )
    code = serializers.CharField(
        label='位置编号',
        validators=[UniqueValidator(queryset=_m.StockWarehouse.objects.filter(is_active=True))]
    )

    class Meta:
        model = _m.StockLocation
        fields = '__all__'
        read_only_fields = ('create_time', 'is_active')
