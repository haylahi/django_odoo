from datetime import datetime

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Task(models.Model):
    """
    In [12]: boss.has_perm('view_task',task)
    Out[12]: False

    In [13]: from guardian.shortcuts import assign_perm

    In [14]: assign_perm('view_task',joe,task)
    Out[14]: <UserObjectPermission: Task object (1) | joe | view_task>

    In [15]: joe.has_perm('view_task',task)
    Out[15]: True

    In [16]: from django.contrib.auth.models import Group

    In [17]: group = Group.objects.create(name='staff')

    In [18]: assign_perm('change_task',group, task)
    Out[18]: <GroupObjectPermission: Task object (1) | staff | change_task>

    In [19]: joe.has_perm('change_task',task)
    Out[19]: False

    In [20]: joe.groups.add(group)

    In [21]: joe.has_perm('change_task',task)
    Out[21]: True

    In [22]:

    """
    summary = models.CharField('标题', max_length=255)
    content = models.TextField('内容')
    create_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    create_time = models.DateTimeField('创建时间', default=datetime.now)

    def __str__(self):
        return self.summary

    class Meta:
        ordering = ['summary', '-create_time']
        permissions = (
            ('view_task', '查看任务'),
        )
