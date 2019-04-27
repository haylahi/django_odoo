# author: Liberty
# date: 2019/4/22 20:31

import json
import logging
from pathlib import WindowsPath, PurePosixPath
import platform

from django.contrib.auth.models import BaseUserManager

__logger__ = logging.getLogger(__name__)

ORDER_STATE = [
    ('cancel', '取消'),
    ('draft', '草稿'),
    ('submitted', '提交审核后'),
    ('in_review', '审核中'),
    ('completed', '审核完成'),
    ('done', '单据完成'),
    ('locked', '锁定')
]

DEFAULT_STATE = 'draft'

SEND_SUCCESS_DATA = {
    'code': '0',
    'message': 'success.',
}

SEND_ERROR_DATA = {
    'code': '1',
    'message': 'error.'
}


def make_success_resp():
    return json.dumps(SEND_SUCCESS_DATA)


def make_error_resp(message: str = None):
    if message is not None:
        _d = SEND_ERROR_DATA.update({'message': message})
    return json.dumps(SEND_ERROR_DATA)


def generate_random_code():
    import time
    import hashlib
    import random
    m = hashlib.md5(str(time.clock()).encode('utf8'))
    m = m.hexdigest()
    r = random.randint(0, 999999)
    return '{r:0>6d}{m}'.format(r=r, m=m)


def make_correct_path(root_path, file_path):
    if platform.system() == 'Windows':
        path = WindowsPath(root_path).joinpath(file_path)
        return path
    else:
        path = PurePosixPath(root_path).joinpath(file_path)
        return path


class MyUserManager(BaseUserManager):
    def _create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError('The given username must be set')
        username = self.model.normalize_username(username)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(username, password, **extra_fields)


def check_float(val: str) -> bool:
    try:
        float(val)
        return True
    except ValueError as e:
        __logger__.error(e)
        return False
