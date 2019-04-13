# author: Liberty
# date: 2019/4/13 16:39

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import UserProfile, BaseCountry, BaseProvince
from .utils import STR_DATETIME_FORMAT


class UserRegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(
        required=True, label='邮箱',
        validators=[UniqueValidator(queryset=UserProfile.objects.filter(is_active=True))]
    )
    password = serializers.CharField(required=True, label='密码')

    def update(self, instance, validated_data):
        """更新"""
        raise SystemError('unsupported operation')

    def create(self, validated_data: dict):
        return UserProfile.objects.create_user(**validated_data)


class CountrySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True, label='id')
    name = serializers.CharField(label='国家', validators=[UniqueValidator(queryset=BaseCountry.objects.all())])
    code = serializers.CharField(label='编码', validators=[UniqueValidator(queryset=BaseCountry.objects.all())])
    short_name = serializers.CharField(label='简称', validators=[UniqueValidator(queryset=BaseCountry.objects.all())])
    area_code = serializers.CharField(label='国家区号', validators=[UniqueValidator(queryset=BaseCountry.objects.all())])
    national_flag = serializers.ImageField(use_url=True, required=False)
    create_time = serializers.DateTimeField(read_only=True, format=STR_DATETIME_FORMAT)

    def update(self, obj: BaseCountry, validated_data: dict):
        if validated_data.get('name') != obj.name:
            raise ValueError("can't modify the country name")

        obj.code = validated_data.get('code', obj.code)
        obj.short_name = validated_data.get('short_name', obj.short_name)
        obj.area_code = validated_data.get('area_code', obj.area_code)
        obj.national_flag = validated_data.get('national_flag', obj.national_flag)
        obj.save()
        return obj

    def create(self, validated_data):
        # 验证 必填字段
        if validated_data.get('name', None) is None:
            raise ValueError('name is required')

        return BaseCountry.objects.create(**validated_data)


class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseProvince
        fields = '__all__'
