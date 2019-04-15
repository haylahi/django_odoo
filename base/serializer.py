# author: Liberty
# date: 2019/4/13 16:39

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import UserProfile, BaseCountry, BaseProvince, BaseUnit, \
    Company, Partner, BaseTax, Currency, CurrencyRate, BaseCity, BaseSequence


class UserRegisterSerializer(serializers.Serializer):
    company = serializers.PrimaryKeyRelatedField(queryset=Company.objects.filter(is_active=True), many=False)
    email = serializers.EmailField(
        required=True, label='邮箱',
        validators=[UniqueValidator(queryset=UserProfile.objects.filter(is_active=True))]
    )
    password = serializers.CharField(required=True, label='密码')

    def update(self, instance, validated_data):
        raise serializers.ValidationError('[ERROR] unsupported operation')

    def create(self, validated_data: dict):
        return UserProfile.objects.create_user(**validated_data)


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseCountry
        fields = '__all__'


class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseProvince
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseCity
        fields = '__all__'


class BaseUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseUnit
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

    # 创建公司的同时创建partner
    def create(self, validated_data):
        ret = super().create(validated_data)
        Partner.objects.create(company=ret, name=ret.name, code=ret.code, create_time=ret.create_time)
        return ret


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = '__all__'


class BaseTaxSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseTax
        fields = '__all__'


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = '__all__'


class CurrencyRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyRate
        fields = '__all__'


class BaseSequenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseSequence
        fields = '__all__'

    def create(self, validated_data):
        prefix = validated_data.get('prefix')
        suffix = validated_data.get('suffix', None)
        if suffix is not None:
            b = BaseSequence.check_format_value(suffix)
            if b is False:
                raise serializers.ValidationError('格式化字符错误')
        ret = BaseSequence.check_format_value(prefix)
        if ret is False:
            raise serializers.ValidationError('格式化字符错误')
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # 验证格式化字符串
        return super().update(instance, validated_data)
