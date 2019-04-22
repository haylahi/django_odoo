# author: Liberty
# date: 2019/4/22 23:04

from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from base import models


def check_float(val: str):
    try:
        float(val)
        return True
    except:
        return False


class BaseUnitSerializer(serializers.Serializer):
    name = serializers.CharField(
        required=True, label='单位',
        validators=[UniqueValidator(queryset=models.BaseUnit.objects.filter(is_active=True))]
    )
    unit_symbol = serializers.CharField(required=True, label='单位')
    unit_type = serializers.CharField(required=True, label='单位类型')
    is_base_unit = serializers.BooleanField(default=False, label='是否为基本单位')
    rounding = serializers.CharField(label='精度', required=True)
    factor = serializers.CharField(label='倍数', required=True)
    compute_method = serializers.CharField(label='计算方式', required=True)

    def create(self, attr):
        if attr.get('unit_type') not in models.CHOICES_UNIT_TYPE:
            raise serializers.ValidationError('error: unit_type is not correct.')
        if attr.get('compute_method') not in models.CHOICES_COMPUTE_METHOD:
            raise serializers.ValidationError('error: compute_method is not correct.')
        if check_float(attr.get('factor')) is False:
            raise serializers.ValidationError('error: factor is not correct')
        if check_float(attr.get('rounding')) is False:
            raise serializers.ValidationError('error: rounding is not correct')
        return models.BaseUnit.objects.create(**attr)

    def update(self, instance, attr):
        pass
