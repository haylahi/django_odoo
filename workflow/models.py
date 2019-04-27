from django.db import models


class Workflow(models.Model):
    """
    工作流
    """
    name = models.CharField('工作流名称', max_length=255)
    description = models.CharField('描述', max_length=255)
    flow_chart = models.CharField('流程图路径', max_length=255, default='')
