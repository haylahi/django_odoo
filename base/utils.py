# author: Liberty
# date: 2019/4/22 20:31

import hashlib
import json
import logging
import platform
import random
import time
from pathlib import WindowsPath, PurePosixPath

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


def create_file(path, content):
    __logger__.info('create a new file...')
    with open(path, 'wb') as f:
        f.write(content)


# -----------------------------------------------------------------------------


from django.conf import settings
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from base import models

PAGE_DICT_DATA = 'currentData'
PAGE_DICT_MODEL = 'currentModel'
PAGE_DICT_COUNT = 'dataCount'

FRONT_NAME = 'name'
FRONT_DATA = 'data'
FRONT_LABEL = 'label'
FRONT_TYPE = 'type'
FRONT_INDEX = 'index'
FRONT_CHOICES = 'choices'
FRONT_MODEL = 'model'

FRONT_BOOL_TRUE_STR = '是'
FRONT_BOOL_FALSE_STR = '否'


def get_model_files(instance):
    """获取模型的附件对象列表"""
    # noinspection PyProtectedMember
    app_label, model_name = instance._meta.app_label, instance._meta.model_name
    model_id = instance.id
    _ret = models.FileObject.objects.filter(
        is_active=True, app_label=app_label,
        model_name=model_name, model_id=model_id
    )
    return _ret


def _get_app_model(model_obj):
    return '{app_label}.{model_name}'.format(
        app_label=model_obj._meta.app_label,
        model_name=model_obj._meta.model_name
    )


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


def get_page_dict(request, obj_list, page_size, field_list=None):
    current_page_number, _field_list = request.GET.get(settings.PAGE_STR, 1), field_list
    paginator = Paginator(obj_list, page_size, settings.PAGE_OFFSET)
    try:
        current_page_obj = paginator.page(current_page_number)
    except (PageNotAnInteger, EmptyPage):
        current_page_obj = paginator.page(1)

    if _field_list is None:
        _field_list = obj_list.model._meta.fields

    return {
        PAGE_DICT_COUNT: paginator.count,
        'pageCount': paginator.num_pages,
        'currentPage': current_page_obj.number,
        PAGE_DICT_DATA: generate_table_data(current_page_obj.object_list, _field_list),
        PAGE_DICT_MODEL: _get_app_model(obj_list.model),
        'hasPrev': current_page_obj.has_previous(),
        'hasNext': current_page_obj.has_next(),
    }


def generate_table_data(obj_list, field_list):
    model_obj, data_list = obj_list.model, list()

    _error = _check_field_name(model_obj, field_list)
    if _error is not True:
        raise ValueError('ERROR: 字段列表错误 错误字段有：{}'.format(_error))

    for index, field_str in enumerate(field_list):
        val = generate_field_header(model_obj, obj_list, field_str, index)
        data_list.append(val)

    return data_list


def generate_field_header(model_obj, obj_list, field_name, index):
    _result = dict()

    # common attrs
    field_object = model_obj._meta.get_field(field_name)
    field_label = field_object.verbose_name if field_object.verbose_name else field_object.name
    is_primary_key = field_object.primary_key  # true or false

    _result[FRONT_NAME] = field_object.name
    _result[FRONT_LABEL] = field_label
    _result[FRONT_INDEX] = index

    if isinstance(field_object, models.CharField):
        field_choices = getattr(field_object, 'choices', [])

        # 判断是否为choices类型
        if len(field_choices) == 0:
            _result[FRONT_TYPE] = 'string'

        else:
            _choices_list = []
            for c in field_choices:
                _choice_dict = dict()
                _choice_dict['value'] = c[0]
                _choice_dict['name'] = c[1]
                _choices_list.append(_choice_dict)
            _result[FRONT_TYPE] = 'choices'
            _result[FRONT_CHOICES] = _choices_list

    if isinstance(field_object, models.ForeignKey):
        fk_model_obj = field_object.related_model

        _result[FRONT_TYPE] = 'm2o'
        _result[FRONT_MODEL] = _get_app_model(fk_model_obj)

    if isinstance(field_object, models.IntegerField):
        _result[FRONT_TYPE] = 'integer'

    if isinstance(field_object, models.BooleanField):
        _result[FRONT_TYPE] = 'boolean'

    if isinstance(field_object, models.DateTimeField):
        _result[FRONT_TYPE] = 'datetime'

    if isinstance(field_object, models.DateField):
        _result[FRONT_TYPE] = 'date'

    if is_primary_key:
        _result[FRONT_TYPE] = 'id'

    if isinstance(field_object, models.ManyToManyField):
        m2m_model_obj = field_object.related_model

        _result[FRONT_TYPE] = 'm2m'
        _result[FRONT_MODEL] = _get_app_model(m2m_model_obj)

    _val = generate_table_body(obj_list, field_object, _result[FRONT_TYPE])
    _result[FRONT_DATA] = _val

    return _result


def generate_table_body(obj_list, field_obj, field_type):
    _value_list, field_name = list(), field_obj.name

    if len(obj_list) == 0:
        return _value_list

    for index, obj in enumerate(obj_list):
        _cell_dict = dict()

        # index
        _cell_dict[FRONT_INDEX] = index

        if field_type in ['string', 'choices', 'integer', 'id']:
            _cell_dict[FRONT_DATA] = getattr(obj, field_name, '')

        if field_type == 'm2o':
            fk_model_instance = getattr(obj, field_name, None)
            fk_model_id = field_obj._related_fields[0][1].name
            _cell_dict[FRONT_DATA] = str(fk_model_instance) if fk_model_instance else ''
            _cell_dict['model_id'] = getattr(fk_model_instance, fk_model_id, '')

        if field_type == 'boolean':
            _b = getattr(obj, field_name)
            _cell_dict[FRONT_DATA] = FRONT_BOOL_TRUE_STR if _b else FRONT_BOOL_FALSE_STR

        if field_type in ['datetime', 'date']:
            _date = getattr(obj, field_name, None)
            if _date:
                _cell_dict[FRONT_DATA] = _date.strftime(FORMAT_DATETIME) \
                    if field_type == 'datetime' else _date.strftime(FORMAT_DATE)
            else:
                _cell_dict[FRONT_DATA] = ''

        if field_type == 'm2m':
            m2m_model_list = getattr(obj, field_name).all().filter(is_active=True)
            m2m_model_id = list(filter(lambda x: x.primary_key == True, field_obj.related_model._meta.fields))[0].name
            if len(m2m_model_list) == 0:
                _cell_dict[FRONT_DATA] = []
            _cell_dict[FRONT_DATA] = [{'name': str(obj), 'value': getattr(obj, m2m_model_id)} for obj in m2m_model_list]

        _value_list.append(_cell_dict)

    return _value_list


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

# class CusTableHeader:
#     """
#     自定义表头
#
#     TODO  重新编写 返回集 表头信息只返回一次 分页信息， 附加信息， 表头信息 真实内容
#
#     """
#
#     def __init__(self):
#         self.model_object = None
#         self.model_field_list = []
#         self.model_data = None
