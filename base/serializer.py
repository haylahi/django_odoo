# author: Liberty
# date: 2019/4/13 16:39

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import (
    BaseCountry, BaseProvince, BaseCity, BaseUnit,
    Currency, CurrencyRate, BaseTax, Company, Partner
)
from .utils import get_field_desc


# -----------------------------国家省市--------------------------------------------


class CountrySerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        label=get_field_desc(BaseCountry, 'name'),
        validators=[UniqueValidator(queryset=BaseCountry.objects.filter(is_active=True), message='国家的名称必须唯一')]
    )
    short_name = serializers.CharField(
        label=get_field_desc(BaseCountry, 'short_name'),
        validators=[UniqueValidator(queryset=BaseCountry.objects.filter(is_active=True))]
    )
    area_code = serializers.CharField(
        label=get_field_desc(BaseCountry, 'area_code'),
        validators=[UniqueValidator(queryset=BaseCountry.objects.filter(is_active=True))]
    )
    is_active = serializers.BooleanField(default=True)

    class Meta:
        model = BaseCountry
        fields = '__all__'

    def update(self, instance: BaseCountry, attr: dict):
        """只可以修改图标"""
        instance.national_flag = attr.get('national_flag', instance.national_flag)
        instance.save()
        return instance


class ProvinceSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(default=True)

    class Meta:
        model = BaseProvince
        fields = '__all__'

    def create(self, validated_data: dict):
        country = validated_data.get('country')
        name = validated_data.get('name')
        short_name = validated_data.get('short_name')
        _n = BaseProvince.objects.filter(is_active=True, country=country, name=name).exists()
        _s = BaseProvince.objects.filter(is_active=True, country=country, short_name=short_name).exists()
        if _n:
            raise serializers.ValidationError('ERROR: 在同一个国家下，不能有两个一样的省')
        if _s:
            raise serializers.ValidationError('ERROR: 在同一个国家下，省的简称是唯一的')
        return super(ProvinceSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        raise serializers.ValidationError('ERROR：暂不支持的操作...')


class CitySerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(default=True)

    class Meta:
        model = BaseCity
        fields = '__all__'

    def create(self, validated_data):
        province = validated_data.get('province')
        name = validated_data.get('name')
        area_code = validated_data.get('area_code')
        car_number = validated_data.get('car_number')
        is_provincial_capital = validated_data.get('is_provincial_capital')

        _n = BaseCity.objects.filter(is_active=True, province=province, name=name).exists()
        _a = BaseCity.objects.filter(is_active=True, area_code=area_code).exists()
        _c = BaseCity.objects.filter(is_active=True, province=province, car_number=car_number).exists()
        _i = BaseCity.objects.filter(is_active=True, province=province, is_provincial_capital=True).exists()

        if _n or _a or _c:
            raise serializers.ValidationError('ERROR: unique error')

        if _i:
            if is_provincial_capital:
                raise serializers.ValidationError('ERROR: 一个省只能有一个省会...')

        return super(CitySerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        raise serializers.ValidationError('ERROR：暂不支持的操作...')


# -----------------------------------------------------------------------------


class UnitSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(default=True)
    code = serializers.CharField(
        label=get_field_desc(BaseUnit, 'code'),
        validators=[UniqueValidator(queryset=BaseUnit.objects.filter(is_active=True), message='单位编码必须唯一')]
    )

    def create(self, validated_data):
        factor = validated_data.get('factor', None)
        if factor is not None:
            try:
                float(factor)
            except:
                raise serializers.ValidationError('ERROR: type of factor is error')
        rounding = validated_data.get('rounding', None)
        if rounding is not None:
            try:
                float(rounding)
            except:
                raise serializers.ValidationError('ERROR: type of rounding is error')

        return super(UnitSerializer, self).create(validated_data)

    class Meta:
        model = BaseUnit
        fields = '__all__'


class CurrencySerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(default=True)
    name = serializers.CharField(
        label=get_field_desc(Currency, 'name'),
        validators=[UniqueValidator(queryset=Currency.objects.filter(is_active=True))]
    )
    code = serializers.CharField(
        label=get_field_desc(Currency, 'code'),
        validators=[UniqueValidator(queryset=Currency.objects.filter(is_active=True))]
    )

    class Meta:
        model = Currency
        fields = '__all__'

    def create(self, validated_data):
        rounding = validated_data.get('rounding', None)
        if rounding is not None:
            try:
                float(rounding)
            except:
                raise serializers.ValidationError('ERROR: type of rounding is error')
        return super(CurrencySerializer, self).create(validated_data)


class CurrencyRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyRate
        fields = '__all__'
        read_only_fields = ('create_time', 'is_active')

    def create(self, validated_data):
        rate = validated_data.get('rate', None)
        if rate is not None:
            try:
                float(rate)
            except:
                raise serializers.ValidationError('ERROR: type of rate is error')
        return super(CurrencyRateSerializer, self).create(validated_data)


class TaxSerializer(serializers.ModelSerializer):
    code = serializers.CharField(
        label=get_field_desc(BaseTax, 'code'),
        validators=[UniqueValidator(queryset=BaseTax.objects.filter(is_active=True))]
    )

    class Meta:
        model = BaseTax
        fields = '__all__'
        read_only_fields = ('is_active',)

    def create(self, validated_data):
        factor = validated_data.get('factor', None)
        if factor is not None:
            try:
                float(factor)
            except:
                raise serializers.ValidationError('ERROR: type of factor is error')
        rounding = validated_data.get('rounding', None)
        if rounding is not None:
            try:
                float(rounding)
            except:
                raise serializers.ValidationError('ERROR: type of rounding is error')
        return super(TaxSerializer, self).create(validated_data)


class CompanySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(
        required=True, label=get_field_desc(Company, 'name'),
        validators=[UniqueValidator(queryset=Company.objects.filter(is_active=True))]
    )
    code = serializers.CharField(
        required=True, label=get_field_desc(Company, 'code'),
        validators=[UniqueValidator(queryset=Company.objects.filter(is_active=True))]
    )
    is_active = serializers.BooleanField(default=True, read_only=True)
    parent_company = serializers.PrimaryKeyRelatedField(
        label=get_field_desc(Company, 'parent_company'),
        many=False, allow_null=True, queryset=Company.objects.filter(is_active=True)
    )
    default_tax = serializers.PrimaryKeyRelatedField(
        label=get_field_desc(Company, 'default_tax'),
        many=False, allow_null=True, queryset=BaseTax.objects.filter(is_active=True)
    )
    default_currency = serializers.PrimaryKeyRelatedField(
        label=get_field_desc(Company, 'default_currency'),
        many=False, allow_null=True, queryset=Currency.objects.filter(is_active=True)
    )

    class Meta:
        model = Company
        fields = '__all__'

    def create(self, attr: dict):
        company = super(CompanySerializer, self).create(attr)
        Partner.objects.create(
            company=company, name=company.name,
            code=company.code, create_time=company.create_time, is_active=True
        )
        return company

    def update(self, instance: Company, attr):
        instance.dummy_discount = attr.get('dummy_discount', instance.dummy_discount)
        instance.default_tax = attr.get('default_tax', instance.default_tax)
        instance.save()
        return instance
