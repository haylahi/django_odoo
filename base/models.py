from datetime import datetime

from django.contrib.auth.models import AbstractBaseUser
from django.db.models import Model, CharField, BooleanField, DateTimeField

from base.utils import MyUserManager

"""
Company



"""


class Company(Model):
    # 空字符串不为 None
    name = CharField('Company', max_length=255, default='')
    code = CharField('Code', max_length=255, default='')

    create_time = DateTimeField('创建时间', default=datetime.now)
    is_active = BooleanField(default=True)

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

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return True

    class Meta:
        ordering = ['-create_time']
        db_table = 'base_user'
