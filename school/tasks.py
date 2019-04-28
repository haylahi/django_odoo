# author: Liberty
# date: 2019/4/28 18:46
import logging
import os

from celery import task

__logger__ = logging.getLogger(__name__)

# 设置 django 执行环境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'powerful.settings')

import django

django.setup()

from . import models


# noinspection PyCallingNonCallable
@task
def create_score_records(task_name, **kwargs):
    """创建学生成绩表"""
    __logger__.info('start celery task {}'.format(task_name))

    # 1. 获取数据
    examination = kwargs.get('examination')
    student_list = kwargs.get('student_list')
    full_score_tag = kwargs.get('full_score_tag')
    create_time = kwargs.get('create_time')
    create_teacher = kwargs.get('create_teacher')

    # 2. 准备数据
    _record_obj_list = []
    for stu in student_list:
        attr = {
            'examination': examination,
            'student': stu,
            'full_score_tag': full_score_tag,
            'create_teacher': create_teacher,
            'create_time': create_time,
            'is_active': True
        }
        _record_obj_list.append(models.ScoreRecord(**attr))
    _ret = models.ScoreRecord.objects.bulk_create(_record_obj_list)
    if len(_ret) == len(student_list):
        # 3. 更改 examination is_create_record
        examination.is_create_record = True
        examination.save()
        return True
    else:
        return False
