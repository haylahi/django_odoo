from datetime import datetime

from django.db import models

from base.models import Company

CHOICES_LOCATION_TYPE = [
    ('VIEW', '视图位置'),
    ('INTERNAL', '内部位置'),
    ('SUPPLIER', '供应商位置'),
    ('CUSTOMER', '客户位置'),
    ('PRODUCTION', '生产位置'),
]

DEFAULT_LOCATION_TYPE = 'INTERNAL'


# ---------------------------------------------------------------------------------------------------------------------


class StockWarehouse(models.Model):
    name = models.CharField('仓库名称', max_length=255, null=True, blank=True)
    code = models.CharField('唯一编码', max_length=255, unique=True)
    short_name = models.CharField('简称', max_length=255, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True, verbose_name='所在公司')
    address = models.CharField('仓库地址', max_length=255, null=True, blank=True)

    create_time = models.DateTimeField('创建时间', default=datetime.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-name']
        db_table = 'stock_warehouse'


class StockLocation(models.Model):
    warehouse = models.ForeignKey('StockWarehouse', on_delete=models.CASCADE, null=True, blank=True, verbose_name='所属仓库')
    name = models.CharField('仓库名称', max_length=255, null=True, blank=True)
    code = models.CharField('唯一编码', max_length=255, unique=True)
    location_type = models.CharField('位置类型', max_length=255, choices=CHOICES_LOCATION_TYPE, default=DEFAULT_LOCATION_TYPE)
    is_return_location = models.BooleanField('是否为退货位置', default=False)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, verbose_name='上级位置', related_name='childs')

    pos_x = models.CharField('X', max_length=255, null=True, blank=True)
    pos_y = models.CharField('Y', max_length=255, null=True, blank=True)
    pos_z = models.CharField('Z', max_length=255, null=True, blank=True)
    create_time = models.DateTimeField('创建时间', default=datetime.now)
    is_active = models.BooleanField(default=True)

    def get_child_locations(self):
        return self.childs.all().filter(is_active=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-name']
        db_table = 'stock_location'
