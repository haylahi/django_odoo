from datetime import datetime

from django.db import models

from base.models import UserProfile

"""
产品标签

"""


class ProductBrand(models.Model):
    name = models.CharField('产品品牌', max_length=255)
    code = models.CharField('编号', max_length=255, default='')
    create_time = models.DateTimeField('创建时间', default=datetime.now)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-name']
        db_table = 'product_brand'


class ProductCategory(models.Model):
    name = models.CharField('产品类别', max_length=255)
    code = models.CharField('编号', max_length=255, default='')
    create_time = models.DateTimeField('创建时间', default=datetime.now)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-name']
        db_table = 'product_category'


class ProductTag(models.Model):
    name = models.CharField('产品标签', max_length=255)
    code = models.CharField('编号', max_length=255, default='')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='所属用户', related_name='product_tags')

    create_time = models.DateTimeField('创建时间', default=datetime.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-name']
        db_table = 'product_tag'


class ProductProduct(models.Model):
    name = models.CharField('产品标签', max_length=255)
    code = models.CharField('编号', max_length=255, default='')

    brand = models.ForeignKey(ProductBrand, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='所属品牌')
    category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='所属类别')
    tags = models.ManyToManyField(ProductTag, verbose_name='标签', blank=True)

    def __str__(self):
        return '{} [{}]'.format(self.name, self.code)

    class Meta:
        ordering = ['-name']
        db_table = 'product_product'
