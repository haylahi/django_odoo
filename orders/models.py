import datetime

from django.db import models

from base.models import Company, Partner


class PurchaseOrder(models.Model):
    """采购订单"""
    name = models.CharField('采购单号', max_length=255)
    origin = models.CharField('源单据', max_length=255, null=True, blank=True)

    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='所属公司')
    partner = models.ForeignKey(Partner, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='客户')

    create_time = models.DateTimeField('创建时间', default=datetime.datetime.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-create_time']
        db_table = 'order_purchase'


class PurchaseOrderLine(models.Model):
    """采购单明细"""
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE, verbose_name='采购单', related_name='purchase_lines')
    create_time = models.DateTimeField('创建时间', default=datetime.datetime.now)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-create_time']
        db_table = 'order_purchase_line'


# ---------------------------------------------------------------------------------------------------------------------


class SaleOrder(models.Model):
    """销售单"""
    name = models.CharField('销售单号', max_length=255)
    origin = models.CharField('源单据', max_length=255, null=True, blank=True)

    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='所属公司')
    partner = models.ForeignKey(Partner, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='客户')

    create_time = models.DateTimeField('创建时间', default=datetime.datetime.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-create_time']
        db_table = 'order_sale'


class SaleOrderLine(models.Model):
    """销售单明细"""
    sale_order = models.ForeignKey(SaleOrder, on_delete=models.CASCADE, verbose_name='销售单', related_name='sale_lines')
    create_time = models.DateTimeField('创建时间', default=datetime.datetime.now)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-create_time']
        db_table = 'order_sale_line'


