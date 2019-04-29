# author: Liberty
# date: 2019/4/22 20:31

import hashlib
import json
import logging
import platform
import random
import time
from datetime import datetime, date
from pathlib import WindowsPath, PurePosixPath

from base import models

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
FORMAT_DATETIME = '%Y-%m-%d %H:%M:%S'
FORMAT_DATE = '%Y-%m-%d'
SEND_SUCCESS_DATA = {
    'code': '0',
    'message': 'success.',
}
SEND_ERROR_DATA = {
    'code': '1',
    'message': 'error.'
}
FRONT_INDEX_STR = 'front_index'
FRONT_DISPLAY_STR = 'display'
FRONT_LABEL_STR = 'label'
FRONT_TYPE_STR = 'type'
FRONT_PRIMARY_KEY_STR = 'primary_key'
FRONT_EDITABLE_STR = 'editable'


def make_success_resp():
    return json.dumps(SEND_SUCCESS_DATA)


def make_error_resp(message: str = None):
    if message is not None:
        _d = SEND_ERROR_DATA.update({'message': message})
    return json.dumps(SEND_ERROR_DATA)


def generate_random_code():
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


def check_float(val: str) -> bool:
    try:
        float(val)
        return True
    except ValueError as e:
        __logger__.error(e)
        return False


def get_model_files(model_obj):
    # noinspection PyProtectedMember
    app_label, model_name = model_obj._meta.app_label, \
                            model_obj._meta.model_name
    model_id = model_obj.id
    _ret = models.FileObject.objects.filter(
        is_active=True, app_label=app_label,
        model_name=model_name, model_id=model_id
    )
    return _ret


def get_field_dict(model_obj):
    _fields = []
    for f in model_obj._meta.fields:
        _fields.append(f.name)
    _d = {}
    for attr in _fields:
        if isinstance(getattr(model_obj, attr), datetime):
            _d[attr] = getattr(model_obj, attr).strftime(FORMAT_DATETIME)
        elif isinstance(getattr(model_obj, attr), date):
            _d[attr] = getattr(model_obj, attr).strftime(FORMAT_DATE)
        else:
            _d[attr] = getattr(model_obj, attr)
    return _d


def create_file(path, content):
    with open(path, 'wb') as f:
        f.write(content)


# -----------------------------------------------------------------------------


def _generate_index_dict(index):
    return {
        'type': 'str',
        'display': index,
        'label': ' No. '
    }


def _generate_field_dict(obj, field_name: str, editable=None):
    """
    char         str
    fk           object
    Int          int
    bool         bool
    m2m          multi
    o2m          multi
    datetime     datetime
    date         date
    choices      multi       select_list
    id           int
    method       method
    """
    _d = dict()
    _f_obj = obj._meta.get_field(field_name)
    _label = _f_obj.verbose_name if _f_obj.verbose_name else _f_obj.name

    if isinstance(_f_obj, models.CharField):
        _choices = getattr(_f_obj, 'choices', [])
        if len(_choices) == 0:
            _d[FRONT_TYPE_STR] = 'str'
            _d[FRONT_DISPLAY_STR] = getattr(obj, field_name, '')
            _d[FRONT_LABEL_STR] = _label
        else:
            _str = getattr(obj, 'get_{}_display'.format(_f_obj.name))()
            _d[FRONT_TYPE_STR] = 'multi'
            _d[FRONT_DISPLAY_STR] = _str
            _d[FRONT_LABEL_STR] = _label
            _d['select_list'] = _choices

    if isinstance(_f_obj, models.ForeignKey):
        fk_obj = getattr(obj, field_name, None)

        _d[FRONT_TYPE_STR] = 'object'
        _d[FRONT_DISPLAY_STR] = str(fk_obj) if fk_obj else ''
        _d[FRONT_LABEL_STR] = _label
        _d['instance'] = fk_obj

    if isinstance(_f_obj, models.IntegerField):
        _d[FRONT_TYPE_STR] = 'int'
        _d[FRONT_DISPLAY_STR] = getattr(obj, field_name, '')
        _d[FRONT_LABEL_STR] = _label

    if isinstance(_f_obj, models.BooleanField):
        _bool = getattr(obj, field_name)

        _d[FRONT_TYPE_STR] = 'bool'
        _d[FRONT_DISPLAY_STR] = '是' if _bool else '否'
        _d[FRONT_LABEL_STR] = _label

    if isinstance(_f_obj, models.DateTimeField):
        _date = getattr(obj, field_name, None)

        _d[FRONT_TYPE_STR] = 'datetime'
        _d[FRONT_DISPLAY_STR] = _date.strftime(FORMAT_DATETIME) if _date else ''
        _d[FRONT_LABEL_STR] = _label

    if isinstance(_f_obj, models.DateField):
        _date = getattr(obj, field_name, None)

        _d[FRONT_TYPE_STR] = 'date'
        _d[FRONT_DISPLAY_STR] = _date.strftime(FORMAT_DATE) if _date else ''
        _d[FRONT_LABEL_STR] = _label

    if isinstance(_f_obj, models.AutoField):
        _d[FRONT_TYPE_STR] = 'int'
        _d[FRONT_DISPLAY_STR] = getattr(obj, field_name)
        _d[FRONT_LABEL_STR] = ' ID '
        _d[FRONT_PRIMARY_KEY_STR] = '1'

    # TODO m2m o2m
    if editable is not None:
        if field_name in editable:
            _d[FRONT_EDITABLE_STR] = '1'

    return _d


def generate_front_list(obj_list, field_list, editable: list = None, index_tag=False) -> list:
    _obj_list, _field_list, _li = obj_list, field_list, list()
    if _obj_list is None:
        return []
    if not isinstance(obj_list, models.Model) and len(obj_list) == 0:
        return []

    if isinstance(_obj_list, models.Model):
        _obj_list = [_obj_list, ]
    for i, o in enumerate(_obj_list, start=1):
        _d = dict()
        if index_tag:
            _d[FRONT_INDEX_STR] = _generate_index_dict(i)
        for f in _field_list:
            _d[f] = _generate_field_dict(o, f)
        _li.append(_d)
    return _li


# -------------------- not raise error -------------------------


class MyUserManager(models.BaseUserManager):
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
