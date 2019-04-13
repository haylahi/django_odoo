# author: Liberty
# date: 2019/4/13 16:39

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import UserProfile


class UserRegister(serializers.Serializer):
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
