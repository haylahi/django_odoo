# author: Liberty
# date: 2019/4/28 22:24

import logging

from django import template
from django.utils.safestring import mark_safe

from base.utils import FRONT_INDEX_STR, FRONT_DISPLAY_STR, FRONT_LABEL_STR

register = template.Library()
_log = logging.getLogger(__name__)

STR_HEADER_CONTENT = """<th>{s}</th>"""
STR_LEVEL_A_BODY = """<tr class="info">"""
STR_LEVEL_D_BODY = """<tr class="danger">"""
STR_LEVEL_NORMAL_BODY = """<tr>"""


@register.simple_tag
def get_field_desc(model_obj, field_name, front=True):
    try:
        ret = model_obj._meta.get_field(field_name).verbose_name
    except Exception as e:
        _log.error(e)
        ret = field_name
    if not front:
        return ret
    return mark_safe(ret)


@register.simple_tag
def generate_table_headers(model_obj, field_list):
    """

    <td><b>序号</b></td>
    {% for f in model_fields %}
        <td><b>{{ f }}</b></td>
    {% endfor %}

    """
    if len(field_list) == 0:
        return ''
    _content = ''
    for f in field_list:
        _s = get_field_desc(model_obj, f, False)
        _s = STR_HEADER_CONTENT.format(s=_s)
        _content = '{c}{s}'.format(c=_content, s=_s)
    return mark_safe(_content)


@register.simple_tag
def get_model_verbose_name(model_obj):
    return mark_safe(model_obj._meta.verbose_name)


@register.simple_tag
def get_display_str(data_dict, field_name, front=True):
    _d = data_dict.get(field_name, {})
    _ret = _d.get(FRONT_DISPLAY_STR, '')
    if front:
        return mark_safe(_ret)
    return _ret


@register.simple_tag
def compute_colorful_table_body(data_dict, field_name, front=True):
    _d = data_dict.get(field_name, {})
    _ret = _d.get(FRONT_DISPLAY_STR, '')
    # TODO 重新方法
    if _ret == 'A':
        return mark_safe(STR_LEVEL_A_BODY)
    if _ret == 'D':
        return mark_safe(STR_LEVEL_D_BODY)
    else:
        return mark_safe(STR_LEVEL_NORMAL_BODY)


@register.simple_tag
def get_index_display(data_dict, front=True):
    return get_display_str(data_dict, FRONT_INDEX_STR, front)


@register.simple_tag
def get_index_label(data_list, front=True):
    data_list = data_list[0]
    _d = data_list.get(FRONT_INDEX_STR, {})
    _ret = _d.get(FRONT_LABEL_STR, '')
    if front:
        return mark_safe(_ret)
    return _ret


@register.simple_tag
def check_front_index(data_list):
    data_list = data_list[0]
    _b = data_list.get(FRONT_INDEX_STR, False)
    return _b

# -----------------------------------------------------------------------------


