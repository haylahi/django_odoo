from datetime import datetime

from django.contrib.auth.models import AbstractBaseUser
from django.db.models import Model, CharField, BooleanField, DateTimeField, ForeignKey, CASCADE

from base.utils import MyUserManager, get_display_name

__all__ = ['Province', 'BaseCity', 'BaseUnit']

"""
Company



"""


class Province(Model):
    name = CharField('省', max_length=255)
    short_name = CharField('简称', max_length=255)
    is_active = BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        db_table = 'base_province'


class BaseCity(Model):
    province = ForeignKey(Province, on_delete=CASCADE, verbose_name='所在省份', related_name='cities')
    name = CharField('城市', max_length=255)
    area_code = CharField('城市区号', max_length=255)
    is_active = BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        db_table = 'base_city'


class BaseUnit(Model):
    name = CharField('单位', max_length=255)
    unit_type = CharField('单位类型', max_length=255)
    is_active = BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['unit_type', 'name']
        db_table = 'base_unit'


class Company(Model):
    name = CharField('Company', max_length=255)
    code = CharField('Code', max_length=255, default='')

    create_time = DateTimeField('创建时间', default=datetime.now)
    is_active = BooleanField(default=True)

    def __str__(self):
        return get_display_name(self.name, self.code)

    class Meta:
        ordering = ['name', '-create_time']
        db_table = 'base_company'


class BaseUser(AbstractBaseUser):
    username = CharField('Username', max_length=255, unique=True)
    email = CharField('Email', max_length=255, default='')
    is_admin = BooleanField(default=False)
    create_time = DateTimeField('创建时间', default=datetime.now)
    is_active = BooleanField(default=True)

    USERNAME_FIELD = 'username'
    objects = MyUserManager()

    def __str__(self):
        return self.username

    # noinspection PyMethodMayBeStatic,PyUnusedLocal
    def has_perm(self, perm, obj=None):
        return True

    # noinspection PyMethodMayBeStatic,PyUnusedLocal
    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return True

    class Meta:
        ordering = ['-create_time']
        db_table = 'base_user'
