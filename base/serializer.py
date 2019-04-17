# author: Liberty
# date: 2019/4/13 16:39

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from base.models import BaseCountry
from .utils import get_field_str


def get_base_model(model_name: str):
    from .utils import get_model
    return get_model('base', model_name)


# -----------------------------------------------------------------------------


class CountrySerializer(serializers.ModelSerializer):
    name = serializers.CharField(label=get_field_str(BaseCountry, 'name'), validators=[UniqueValidator(queryset=BaseCountry.objects.filter(is_active=True))])
    short_name = serializers.CharField(label=get_field_str(BaseCountry, 'short_name'), validators=[UniqueValidator(queryset=BaseCountry.objects.filter(is_active=True))])
    area_code = serializers.CharField(label=get_field_str(BaseCountry, 'area_code'), validators=[UniqueValidator(queryset=BaseCountry.objects.filter(is_active=True))])
    is_active = serializers.BooleanField(default=True)

    class Meta:
        model = BaseCountry
        fields = '__all__'

    def update(self, instance: BaseCountry, attr: dict):
        instance.national_flag = attr.get('national_flag', instance.national_flag)
        instance.save()
        return instance
