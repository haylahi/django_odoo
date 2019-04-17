# author: Liberty
# date: 2019/4/17 23:04

from celery import task

"""
1. 启动 celery 
    python manage.py celery worker -c 4 --loglevel=info
2. 启动 监视器
    python manage.py celery flower

"""


# noinspection PyCallingNonCallable
@task
def task_test(x, y):
    return x + y
