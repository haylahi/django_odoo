from datetime import datetime

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Task(models.Model):
    """
    assume 假设

    """
    summary = models.CharField('标题', max_length=255)
    content = models.TextField('内容')
    create_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    create_time = models.DateTimeField('创建时间', default=datetime.now)

    class Meta:
        db_table = 'test_task'
        permissions = (
            ('view_task', '查看任务'),
        )
