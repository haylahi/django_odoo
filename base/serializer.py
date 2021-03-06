# author: Liberty
# date: 2019/4/22 23:04

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from base import models
from base.utils import check_float

UNIT_TYPE_LIST = [i[0] for i in models.CHOICES_UNIT_TYPE]
COMPUTE_METHOD = [i[0] for i in models.CHOICES_COMPUTE_METHOD]


class BaseUnitSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(
        required=True, label='单位',
        validators=[UniqueValidator(queryset=models.BaseUnit.objects.filter(is_active=True), message='单位的名称不能重复')]
    )
    unit_symbol = serializers.CharField(required=True, label='单位符号')
    unit_type = serializers.CharField(required=True, label='单位类型')
    is_base_unit = serializers.BooleanField(label='是否为基本单位', required=True)
    rounding = serializers.CharField(label='精度', required=True)
    factor = serializers.CharField(label='倍数', required=True)
    compute_method = serializers.CharField(label='计算方式', required=True)

    def create(self, attr):
        if attr.get('unit_type') not in UNIT_TYPE_LIST:
            raise serializers.ValidationError('error: unit_type is not correct.')
        if attr.get('compute_method') not in COMPUTE_METHOD:
            raise serializers.ValidationError('error: compute_method is not correct.')
        if check_float(attr.get('factor')) is False:
            raise serializers.ValidationError('error: factor is not correct')
        if float(attr.get('factor')) == 0:
            raise serializers.ValidationError('error: factor is can\'t be 0')
        if check_float(attr.get('rounding')) is False:
            raise serializers.ValidationError('error: rounding is not correct')

        # 强制修改标准单位
        if attr.get('is_base_unit') is True:
            attr.update({'factor': '1', 'compute_method': models.DEFAULT_COMPUTE_METHOD})

        return models.BaseUnit.objects.create(**attr)

    def update(self, obj: models.BaseUnit, attr: dict):
        # TODO update logic
        return obj
