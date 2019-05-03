# author: Liberty
# date: 2019/4/22 20:31

import hashlib
import json
import logging
import platform
import random
import time
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


def get_model_files(instance):
    """获取模型的附件对象列表"""
    # noinspection PyProtectedMember
    app_label, model_name = instance._meta.app_label, \
                            instance._meta.model_name
    model_id = instance.id
    _ret = models.FileObject.objects.filter(
        is_active=True, app_label=app_label,
        model_name=model_name, model_id=model_id
    )
    return _ret


def create_file(path, content):
    __logger__.info('create a new file...')
    with open(path, 'wb') as f:
        f.write(content)


# -----------------------------------------------------------------------------


FRONT_DATA = 'data'
FRONT_LABEL = 'label'
FRONT_TYPE = 'type'
FRONT_CHOICES = 'choices'
FRONT_MODEL = 'model'
FRONT_MODEL_ID = 'model_id'
FRONT_CHOICES_VALUE = 'value'

FRONT_BOOL_TRUE_STR = '是'
FRONT_BOOL_FALSE_STR = '否'


def _check_field_name(model_obj, field_list):
    """
    检查字段是否存在
    """
    _ret = []
    for f in field_list:
        try:
            model_obj._meta.get_field(f)
        except Exception as e:
            _ret.append(f)
            __logger__.error(e)
    return True if len(_ret) == 0 else _ret


def _get_app_model(model_obj):
    """
    :return 'app.model'

    """
    return '{app_label}.{model_name}'.format(
        app_label=model_obj._meta.app_label,
        model_name=model_obj._meta.model_name
    )


def _generate_field_dict(instance, field_name):
    """
    :param instance: 当前模型的实例对象
    :param field_name: 当前模型的要给字段

    char         str
    fk           object
    Int          int
    bool         bool
    m2m          multi   不显示外键列表 要选择时去获取
    o2m          multi
    datetime     datetime
    date         date
    choices      multi       select_list
    id           int
    method       method
    index        int

    o2m method --> test_records
    o2m filed_list --> ['a','b',...]

    """

    # 1.要返回的字典 2. 当前模型的实例 3. 字段的名称
    _data_dict, _model_instance, _field_name = dict(), instance, field_name

    _field_object = _model_instance._meta.get_field(_field_name)
    field_label_str = _field_object.verbose_name if _field_object.verbose_name else _field_object.name

    if isinstance(_field_object, models.CharField):
        _choices = getattr(_field_object, 'choices', [])
        if len(_choices) == 0:
            _data_dict[FRONT_TYPE] = 'str'
            _data_dict[FRONT_DATA] = getattr(_model_instance, _field_name, '')
            _data_dict[FRONT_LABEL] = field_label_str
        else:
            _str = getattr(_model_instance, 'get_{}_display'.format(_field_object.name))()
            _choices_list = list()
            for c in _choices:
                choice_dict = dict()
                choice_dict['name'] = c[1]
                choice_dict['value'] = c[0]
                _choices_list.append(choice_dict)

            _data_dict[FRONT_TYPE] = 'choices'
            _data_dict[FRONT_DATA] = _str
            _data_dict[FRONT_CHOICES_VALUE] = getattr(_model_instance, _field_object.name, '')
            _data_dict[FRONT_LABEL] = field_label_str
            _data_dict[FRONT_CHOICES] = _choices_list

    if isinstance(_field_object, models.ForeignKey):
        fk_obj = getattr(_model_instance, _field_name, None)

        _data_dict[FRONT_TYPE] = 'm2o'
        _data_dict[FRONT_DATA] = str(fk_obj) if fk_obj else ''
        _data_dict[FRONT_LABEL] = field_label_str
        _data_dict[FRONT_MODEL] = _get_app_model(fk_obj)
        _data_dict[FRONT_MODEL_ID] = fk_obj.id if fk_obj else 0

    if isinstance(_field_object, models.IntegerField):
        _data_dict[FRONT_TYPE] = 'int'
        _data_dict[FRONT_DATA] = getattr(_model_instance, _field_name, '')
        _data_dict[FRONT_LABEL] = field_label_str

    if isinstance(_field_object, models.BooleanField):
        _bool = getattr(_model_instance, _field_name)

        _data_dict[FRONT_TYPE] = 'bool'
        _data_dict[FRONT_DATA] = FRONT_BOOL_TRUE_STR if _bool else FRONT_BOOL_FALSE_STR
        _data_dict[FRONT_LABEL] = field_label_str

    if isinstance(_field_object, models.DateTimeField):
        _date = getattr(_model_instance, _field_name, None)
        _data_dict[FRONT_TYPE] = 'datetime'
        _data_dict[FRONT_DATA] = _date.strftime(FORMAT_DATETIME) if _date else ''
        _data_dict[FRONT_LABEL] = field_label_str

    if isinstance(_field_object, models.DateField):
        _date = getattr(_model_instance, _field_name, None)
        _data_dict[FRONT_TYPE] = 'date'
        _data_dict[FRONT_DATA] = _date.strftime(FORMAT_DATE) if _date else ''
        _data_dict[FRONT_LABEL] = field_label_str

    if isinstance(_field_object, models.AutoField):
        _data_dict[FRONT_TYPE] = 'id'
        _data_dict[FRONT_DATA] = getattr(_model_instance, _field_name)
        _data_dict[FRONT_LABEL] = 'ID'

    if isinstance(_field_object, models.ManyToManyField):
        _model_obj = getattr(_model_instance, _field_object.name).model
        _model_set = getattr(_model_instance, _field_object.name).all().filter(is_active=True)
        if len(_model_set) > 0:
            _data_list = [str(o) for o in _model_set]
            _id_list = [o.id for o in _model_set]
        else:
            _data_list = []
            _id_list = []

        _data_dict[FRONT_TYPE] = 'm2m'
        _data_dict[FRONT_DATA] = _data_list
        _data_dict[FRONT_LABEL] = field_label_str
        _data_dict[FRONT_MODEL] = _get_app_model(_model_obj)
        _data_dict[FRONT_MODEL_ID] = _id_list

    return _data_dict


def generate_result_list(obj_list, field_list):
    """
    为前端生成 result list

    :param obj_list: querySet
    :param field_list: list of fields
    :return: list of data

    """
    _obj_list, _field_list, _result_list = obj_list, field_list, list()
    if len(_field_list) == 0:
        raise ValueError('ERROR: 字段列表不能为空...')
    # 检查querySet
    if _obj_list is None:
        return _result_list
    if not isinstance(obj_list, models.Model) and len(obj_list) == 0:
        return _result_list
    if isinstance(_obj_list, models.Model):
        _obj_list = [_obj_list, ]
    # 检查字段的正确性
    _error = _check_field_name(_obj_list[0], _field_list)
    if _error is not True:
        raise ValueError('ERROR: 字段列表错误 错误字段有：{}'.format(_error))

    for obj in _obj_list:
        _d = dict()
        for f in _field_list:
            _d[f] = _generate_field_dict(obj, f)
        _result_list.append(_d)
    return _result_list


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


class CusTableHeader:
    """自定义表头"""

    def __init__(self):
        self.model_object = None
        self.model_field_list = []
        self.model_data = None
