from django.db import models

from base.models import Company

"""
产品标签

"""


class ProductBrand(models.Model):
    name = models.CharField('产品品牌', max_length=255)
    code = models.CharField('编号', max_length=255)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-name']
        db_table = 'product_brand'


class ProductSeries(models.Model):
    name = models.CharField('产品系列', max_length=255)
    code = models.CharField('编号', max_length=255)
    brand = models.ForeignKey(ProductBrand, on_delete=models.CASCADE, verbose_name='所属品牌')
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)
    is_common_series = models.BooleanField(default=False, verbose_name='通用系列? ')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-name']
        db_table = 'product_series'


class ProductStyle(models.Model):
    name = models.CharField('产品款式', max_length=255)
    code = models.CharField('编号', max_length=255)
    series = models.ForeignKey(ProductSeries, on_delete=models.CASCADE, verbose_name='所属系列')
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-name']
        db_table = 'product_style'
