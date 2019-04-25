import random
from datetime import datetime

from django.contrib.auth import get_user_model
from django.db import models

from base.models import BaseUnit, Company
from base.utils import ORDER_STATE, DEFAULT_STATE

User = get_user_model()

CHOICES_COLOR = [
    ('red', '红'),
    ('blue', '蓝'),
    ('green', '绿'),
    ('yellow', '黄'),
    ('white', '白')
]

CHOICES_PRODUCT_USAGE_TYPE = [
    ('service', '服务类'),
    ('virtual', '虚拟类'),
    ('stock', '库存类'),
]

CHOICES_PRODUCT_SALE_TYPE = [
    ('pre_sale', '预售'),
    ('normal', '正常销售'),
    ('stop', '停售'),
    ('sold_out', '下架'),
]

DEFAULT_PRODUCT_SALE_TYPE = 'normal'


# -------------------------------------------------------------------------------------

class ProductBrand(models.Model):
    """品牌"""
    name = models.CharField('品牌', max_length=255)
    code = models.CharField('代号', max_length=255, default='')
    rank = models.IntegerField('热度', default=1)

    create_time = models.DateTimeField('Create Time', default=datetime.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class ProductCategory(models.Model):
    name = models.CharField('产品类别', max_length=255)
    code = models.CharField('代号', max_length=255, default='')
    rank = models.IntegerField('热度', default=1)

    create_time = models.DateTimeField('Create Time', default=datetime.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class ProductTag(models.Model):
    name = models.CharField('产品标签', max_length=255)
    rank = models.IntegerField('热度', default=1)
    color = models.CharField('标签颜色', max_length=255, choices=CHOICES_COLOR, default='white')
    create_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='产品标签', related_name='user_tags')
    create_time = models.DateTimeField('Create Time', default=datetime.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


# -------------------产品属性------------------------------------------


class Product(models.Model):
    """产品"""
    brand = models.ForeignKey(ProductBrand, on_delete=models.PROTECT, verbose_name='产品品牌', related_name='brand_products')
    category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT, verbose_name='产品标签', related_name='category_products')
    tags = models.ManyToManyField(ProductTag, blank=True)
    company = models.ForeignKey(Company, on_delete=models.PROTECT, verbose_name='所属公司', related_name='company_products')

    # 默认为库存类产品 与公司有关信息 以下四个
    product_usage_type = models.CharField('产品使用方式分类', max_length=255, choices=CHOICES_PRODUCT_USAGE_TYPE, default='stock')
    can_sale = models.BooleanField('能销售', default=True)
    can_purchase = models.BooleanField('能采购', default=True)
    product_sale_type = models.CharField('销售属性', max_length=255, choices=CHOICES_PRODUCT_SALE_TYPE, default=DEFAULT_PRODUCT_SALE_TYPE)

    name = models.CharField('产品名称', max_length=255)
    code = models.CharField('代号', max_length=255, default='')
    desc = models.CharField('产品详细描述', max_length=255, default='')
    barcode = models.CharField('商品条码', max_length=255, default='')

    product_rank = models.IntegerField('产品热度', default=1)

    # TODO 上传附件的接口 显示附件的接口 上传时的文件名处理
    product_image = models.CharField('产品图片路径', max_length=255, default='default_logo.png')

    default_unit_uom = models.ForeignKey(BaseUnit, on_delete=models.PROTECT, verbose_name='产品默认数量单位', related_name='product_default_unit_uom')

    # ------------- 产品基本信息 ---------------------------
    product_length = models.CharField('长', max_length=255)
    product_width = models.CharField('宽', max_length=255)
    product_height = models.CharField('高', max_length=255)
    product_volume_uom = models.ForeignKey(BaseUnit, on_delete=models.PROTECT, verbose_name='产品体积单位', related_name='product_volume_uom')

    create_time = models.DateTimeField('Create Time', default=datetime.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class ProductPriceList(models.Model):
    """需要审核"""
    name = models.CharField('产品价格单', max_length=255, default='ProductPriceList{r:0<4d}'.format(r=random.randint(1, 9999)))
    company = models.ForeignKey(Company, on_delete=models.PROTECT, verbose_name='所属公司')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name='所属产品', related_name='product_price_list')

    price_uom = models.ForeignKey(BaseUnit, on_delete=models.PROTECT, verbose_name='价格单位')
    original_price = models.CharField('成本价', max_length=255, default='1')
    purchase_price = models.CharField('采购价', max_length=255, default='1')
    sale_price = models.CharField('销售价', max_length=255, default='1')

    # 价格生效范围
    start_date = models.DateField('开始时间', default=datetime.now)
    end_date = models.DateField('结束时间', null=True, blank=True)

    create_user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='创建用户')
    create_time = models.DateTimeField('Create Time', default=datetime.now)
    done_time = models.DateTimeField('审核完成时间', null=True, blank=True)

    # TODO 审核逻辑设计  保存审核人信息  审核时间 完成时间
    state = models.CharField('单据状态', max_length=255, choices=ORDER_STATE, default=DEFAULT_STATE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
