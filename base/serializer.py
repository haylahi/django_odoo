# author: Liberty
# date: 2019/4/13 16:39

from rest_framework import serializers


def get_base_model(model_name: str):
    from .utils import get_model
    return get_model('base', model_name)


# -----------------------------------------------------------------------------


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = get_base_model('BaseCountry')
        fields = '__all__'

    def create(self, attrs: dict):
        return super().create(attrs)

    def update(self, instance, validated_data):
        raise serializers.ValidationError('Unsupported Operation: 你暂时不能更新国家的信息...')
