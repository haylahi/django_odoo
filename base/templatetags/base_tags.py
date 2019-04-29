# author: Liberty
# date: 2019/4/28 22:24

import logging

from django import template
from django.utils.safestring import mark_safe

__logger__ = logging.getLogger(__name__)
register = template.Library()

COLOR_CLASS_DICT = {
    'success': 'class="success"',
    'warning': 'class="warning"',
    'danger': 'class="danger"',
    'info': 'class="info"',
    'active': 'class="active"',
}

TAG_TH_STR = """
<th {color} {index} >{char}</th>
"""

STR_TH_ID = """
id="th-0-{}"
"""

TAG_TD_STR = """
<td {color} {index} >{char}</td>
"""

STR_TD_ID = """
id="td-{col}-{row}"
"""

TAG_TABLE_START_STR = """
<table class="table table-hover table-bordered">
"""

TAG_TABLE_END_STR = """
</table>
"""


@register.simple_tag
def get_field_desc(model_class, field_name, front=True):
    try:
        # noinspection PyProtectedMember
        result = model_class._meta.get_field(field_name).verbose_name
    except Exception as e:
        __logger__.error(e)
        result = field_name
    return mark_safe(result) if front else result


@register.simple_tag
def generate_table_header(model_class, field_name, index, front=True):
    _desc = get_field_desc(model_class, field_name, True)
    _color = 'none'

    # 开启id
    _id_tag = True
    if not _id_tag:
        index = ''
    else:
        index = STR_TH_ID.format(index)

    _tag = TAG_TH_STR.format(color=COLOR_CLASS_DICT.get(_color, ''), index=index, char=_desc)
    return mark_safe(_tag) if front else _tag


@register.simple_tag
def generate_table_body(model_obj, field_name, col_index, row_index, front=True):
    _data = getattr(model_obj, field_name, '')
    _color = 'none'

    _id_tag = True
    if not _id_tag:
        index = ''
    else:
        index = STR_TD_ID.format(col=col_index, row=row_index)

    if field_name == 'score_level':
        if _data == 'A':
            _color = 'success'
        if _data == 'D':
            _color = 'danger'

    _tag = TAG_TD_STR.format(color=COLOR_CLASS_DICT.get(_color, ''), index=index, char=_data)
    return mark_safe(_tag) if front else _tag


@register.simple_tag
def get_col_index(index, front=True):
    return mark_safe(index) if front else index


@register.simple_tag
def generate_table(model_class, model_data, field_list, front=True):
    _s = TAG_TABLE_START_STR

    # thead
    _s = '{}{}'.format(TAG_TABLE_START_STR, '<thead><tr>')
    for i, f in enumerate(field_list):
        _ret = generate_table_header(model_class, f, i, False)
        _s = '{}{}'.format(_s, _ret)
    _s = '{}{}'.format(_s, '</tr></thead>')

    # tbody
    _s = '{}{}'.format(_s, '<tbody>')
    for col, obj in enumerate(model_data):
        _s = '{}{}'.format(_s, '<tr>')
        for row, f in enumerate(field_list):
            _res = generate_table_body(obj, f, col, row, False)
            _s = '{}{}'.format(_s, _res)
        _s = '{}{}'.format(_s, '</tr>')
    _s = '{}{}'.format(_s, '</tbody>')

    _s = '{}{}'.format(_s, TAG_TABLE_END_STR)
    return mark_safe(_s) if front else _s
