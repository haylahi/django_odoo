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

from school import models


# noinspection PyCallingNonCallable
@task
def create_new_record(task_name, **kwargs):
    __logger__.info('start celery task {}'.format(task_name))

    ret = models.Student.objects.all()
    __logger__.info(ret)

    return 'success'
