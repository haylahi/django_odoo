# author: Liberty
# date: 2019/4/13 14:11

import datetime
import hashlib
import os
import time

from django.conf import settings
from django.contrib.auth.base_user import BaseUserManager
from django.core.files.storage import FileSystemStorage

STR_DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'


class UserProfileManager(BaseUserManager):
    def create_user(self, email, password=None, company=None):
        if not email:
            raise ValueError('请输入正确的邮箱。。。')
        user = self.model(email=self.normalize_email(email), company=company)
        user.set_password(password)
        user.save(using=self._db)
        # 创建一个用户信息
        user.create_user_info()
        return user

    def create_superuser(self, email, password, company=None):
        user = self.create_user(email, password=password, company=company)
        user.is_admin = True
        user.save(using=self._db)
        return user


class CustomFileStorage(FileSystemStorage):

    def __init__(self, location=settings.MEDIA_ROOT, base_url=settings.MEDIA_URL, *args, **kwargs):
        super().__init__(location, base_url, *args, **kwargs)

    def _save(self, name, content):
        _name = name
        _content = content
        suffix = os.path.splitext(_name)[1]
        dir_name = os.path.dirname(_name)
        new_file_name = '{}{}{}'.format(generate_unique_code(), generate_datetime(), suffix)
        _name = os.path.join(dir_name, new_file_name)
        return super()._save(_name, _content)


def generate_unique_code():
    m = hashlib.md5(str(time.clock()).encode('utf-8'))
    return m.hexdigest()


def generate_datetime():
    return datetime.datetime.now().strftime('%Y%m%d%H%M%S')


def compute_float(number: str, rounding: str):
    """
    精度计算

    :param number: 要计算的数
    :param rounding: 精度
    :return: 舍入后的数量
    """
    from decimal import Decimal, ROUND_HALF_UP
    _origin_num = Decimal(number)
    _ret = _origin_num.quantize(Decimal(rounding), rounding=ROUND_HALF_UP)
    return str(_ret)


# ---------------------------------------------------------------------------------------------------------------------


def get_model(app: str, model: str):
    from django.apps import apps
    return apps.get_model(app, model)


def check_base_unique_code(model_name: str, code: str):
    obj = get_model('base', model_name)
    return not obj.objects.filter(is_active=True, code=code).exists()
