# author: Liberty
# date: 2019/4/28 22:24

import logging

from django import template
from django.utils.safestring import mark_safe

register = template.Library()
_log = logging.getLogger(__name__)

STR_HEADER_SEQUENCE = """<td><b>No.</b></td>"""
STR_HEADER_CONTENT = """<td><b>{s}</b></td>"""


def get_field_desc(model_obj, field_name):
    try:
        ret = model_obj._meta.get_field(field_name).verbose_name
    except Exception as e:
        _log.error(e)
        ret = field_name
    return ret


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
    _content = STR_HEADER_SEQUENCE
    for f in field_list:
        _s = get_field_desc(model_obj, f)
        _s = STR_HEADER_CONTENT.format(s=_s)
        _content = '{c}{s}'.format(c=_content, s=_s)
    return mark_safe(_content)
