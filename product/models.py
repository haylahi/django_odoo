from django.db import models

from base.models import Company


class ProductBrand(models.Model):
    name = models.CharField('品牌', max_length=255)
    code = models.CharField('编号', max_length=255)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-name']
        db_table = 'product_brand'


class ProductSeries(models.Model):
    name = models.CharField('系列', max_length=255)
    code = models.CharField('编号', max_length=255)
    brand = models.ForeignKey(ProductBrand, on_delete=models.CASCADE, verbose_name='所属品牌', related_name='own_series')
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-name']
        db_table = 'product_series'
