# author: Liberty
# date: 2019/4/22 23:04

from rest_framework import serializers
from base import models


class BaseUnitSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, label='单位')
    unit_symbol = serializers.CharField(required=True, label='单位')
    unit_type = serializers.CharField(required=True, label='单位类型')
    is_base_unit = serializers.BooleanField(default=False, label='是否为基本单位')
    factor = serializers.CharField(label='倍数', required=True)
    compute_method = serializers.CharField(label='计算方式', required=True)

    def create(self, attr):
        pass

    def update(self, instance, attr):
        pass
