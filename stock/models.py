from datetime import datetime

from django.db import models

from base.models import Company, Province, BaseCity

CHOICES_LOCATION_TYPE = [
    ('supplier', '供应商'),
    ('internal', '内部位置'),
    ('customer', '客户位置'),
    ('return', '退回(作废)位置'),
    ('virtual', '虚拟位置'),
    ('production', '生产位置'),
]

DEFAULT_LOCATION_TYPE = 'internal'


class StockWarehouse(models.Model):
    """
    TODO 仓库和位置之间的关系

    """
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='所属公司', related_name='company_warehouse')
    name = models.CharField('仓库名称', max_length=255)
    short_name = models.CharField('简称', max_length=255, default='')
    code = models.CharField('代号', max_length=255, default='')
    description = models.CharField('描述', max_length=255, default='')

    province = models.ForeignKey(Province, on_delete=models.PROTECT, verbose_name='所在省份')
    city = models.ForeignKey(BaseCity, on_delete=models.PROTECT, verbose_name='所在城市')
    address = models.CharField('详细地址', max_length=255, default='')

    create_time = models.DateTimeField('创建时间', default=datetime.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class StockLocation(models.Model):
    """内部位置"""
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='所属公司', related_name='company_location')
    loc_type = models.CharField('位置类型', max_length=255, choices=CHOICES_LOCATION_TYPE, default=DEFAULT_LOCATION_TYPE)

    name = models.CharField('仓库位置名称', max_length=255)
    short_name = models.CharField('简称', max_length=255, default='')
    code = models.CharField('代号', max_length=255, default='')
    description = models.CharField('描述', max_length=255, default='')

    posx = models.CharField('X', max_length=255, default='')
    posy = models.CharField('Y', max_length=255, default='')
    posz = models.CharField('Z', max_length=255, default='')

    create_time = models.DateTimeField('创建时间', default=datetime.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
