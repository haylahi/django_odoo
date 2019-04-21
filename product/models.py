from datetime import datetime

from django.db import models

from base.models import UserProfile, BaseUnit, Company, Currency
from base.utils import CustomFileStorage

CHOICES_PRODUCT_TYPE = [
    ('STD', '标准产品'),
    ('PART', '零件'),
    ('SERVE', '服务类'),
    ('VIRTUAL', '虚拟类'),
    ('PACKAGE', '包装类(不能单个存在)'),
]

CHOICES_PRODUCT_USAGE_TYPE = [
    ('NORMAL', '正常'),
    ('STOP_SALE', '停售'),
    ('STOP_PRODUCTION', '停产'),
    ('PRE_SALE', '预售'),
    ('SOLD_OUT', '下架'),
    ('DISABLE', '禁用'),
]

CHOICES_STOCK_TRACKING = [
    ('LOT', '批次追踪'),
    ('SERIAL', '序列追踪'),
    ('NONE', '无'),
]

"""

产品标签
产品价格表 配件价格表 价格表针对的公司  色板价格表  配件价格表
产品包装  

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
    name = models.CharField('产品名称', max_length=255)
    code = models.CharField('编号', max_length=255, default='')
    desc = models.CharField('产品描述', max_length=255, default='')
    brand = models.ForeignKey(ProductBrand, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='所属品牌')
    category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='所属类别')

    product_parts = models.ManyToManyField('ProductParts', blank=True, verbose_name='产品配件列表')
    product_display_rank = models.CharField('产品显示排序', default='', max_length=255)

    is_dummy_special_product = models.BooleanField('特殊定制？(虚拟)', default=False)
    product_type = models.CharField('产品属性', max_length=255, choices=CHOICES_PRODUCT_TYPE, default='STD')
    product_usage_type = models.CharField('产品可使用属性', max_length=255, choices=CHOICES_PRODUCT_USAGE_TYPE, default='NORMAL')

    product_volume = models.CharField('产品体积描述', max_length=255, default='')
    product_weight = models.CharField('产品重量描述', max_length=255, default='')

    can_sale = models.BooleanField('可以销售？', default=True)
    can_purchase = models.BooleanField('可以采购？', default=True)
    use_stock = models.BooleanField('使用库存？', default=True)
    stock_tracking = models.CharField('产品库存追踪', max_length=255, choices=CHOICES_STOCK_TRACKING, default='LOT')

    barcode = models.CharField('商品条码', max_length=255, default='')

    """
    产品属性分类  服务类 虚拟类 配件类
    产品外观   体积  重量  
    产品可以使用属性 可生产 可售 停产 等等...
    产品价格表  子公司可以看到的产品列表
    
    """

    product_image = models.ImageField(verbose_name='产品图片', upload_to='product_image/', storage=CustomFileStorage(), default='default_logo.png')

    default_unit_uom = models.ForeignKey(BaseUnit, verbose_name='默认数量单位', on_delete=models.SET_NULL, null=True, blank=True)

    tags = models.ManyToManyField(ProductTag, verbose_name='标签', blank=True)

    create_time = models.DateTimeField('创建时间', default=datetime.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return '{} [{}]'.format(self.name, self.code)

    class Meta:
        ordering = ['-name']
        db_table = 'product_product'


# -----------------------------------------------------------------------------

class ProductPriceList(models.Model):
    """
    产品价格单
    需要审核
    批量产品 的价格
    """
    name = models.CharField('产品价格单', max_length=255)
    code = models.CharField('编号', max_length=255, default='')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='所属公司', related_name='my_product_price_lists')
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, verbose_name='货币')
    date_start = models.DateField('开始日期', default=datetime.today)
    date_end = models.DateField('结束日期', default=datetime.today)

    create_time = models.DateTimeField('创建时间', default=datetime.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['create_time']
        db_table = 'product_price_list'


class ProductPriceItem(models.Model):
    """从表记录ID"""
    price_list = models.ForeignKey(ProductPriceList, on_delete=models.CASCADE, verbose_name='产品价格单', related_name='item_lists')
    product = models.ForeignKey(ProductProduct, on_delete=models.CASCADE, verbose_name='产品', related_name='my_price_items')
    unit_uom = models.ForeignKey(BaseUnit, on_delete=models.CASCADE, verbose_name='单价数量单位')
    rounding = models.CharField('精度', max_length=255, default='0.00')

    """
    mark --> 显示价格
    """
    mark_price = models.CharField('产品标价(指导售价)', max_length=255, default='0')
    sale_price = models.CharField('销售价格', max_length=255, default='0')
    purchase_price = models.CharField('采购价格', max_length=255, default='0')
    standard_price = models.CharField('成本价格', max_length=255, default='0')

    create_time = models.DateTimeField('创建时间', default=datetime.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return '{} ({})'.format(self.product.name, self.standard_price)

    class Meta:
        ordering = ['create_time']
        db_table = 'product_price_item'


# -----------------------------------------------------------------------------

class AppearanceType(models.Model):
    """外观类型"""
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, verbose_name='适用产品类别')
    name = models.CharField('外观类型', max_length=255)
    code = models.CharField('编号', max_length=255, default='')
    create_time = models.DateTimeField('创建时间', default=datetime.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        db_table = 'product_appearance_type'


class AppearanceGroup(models.Model):
    """外观组"""
    appearance_type = models.ForeignKey(AppearanceType, on_delete=models.CASCADE, verbose_name='外观组')

    name = models.CharField('外观组', max_length=255)
    code = models.CharField('编号', max_length=255, default='')
    create_time = models.DateTimeField('创建时间', default=datetime.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        db_table = 'product_appearance_group'


class AppearanceItem(models.Model):
    appearance_group = models.ForeignKey(AppearanceGroup, on_delete=models.CASCADE, verbose_name='所属外观组', related_name='own_items')
    name = models.CharField('外观', max_length=255)
    code = models.CharField('编号', max_length=255, default='')
    create_time = models.DateTimeField('创建时间', default=datetime.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        db_table = 'product_appearance_item'


class AppearanceMap(models.Model):
    """
    外观选配
    need approve
    """
    product = models.ForeignKey(ProductProduct, on_delete=models.CASCADE, verbose_name='产品', related_name='own_appearance')

    looks_type = models.ForeignKey(AppearanceType, on_delete=models.CASCADE)
    looks_group = models.ForeignKey(AppearanceGroup, on_delete=models.CASCADE, null=True, blank=True)
    looks_items = models.ManyToManyField(AppearanceItem, blank=True, verbose_name='选配外观', related_name='looks_items_map')
    exclude_looks_items = models.ManyToManyField(AppearanceItem, blank=True, verbose_name='排除外观', related_name='exclude_looks_items_map')

    create_time = models.DateTimeField('创建时间', default=datetime.now)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['create_time']
        db_table = 'product_appearance_map'


class AppearanceItemPriceList(models.Model):
    name = models.CharField('外观价格单', max_length=255)
    code = models.CharField('编号', max_length=255, default='')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='所属公司', related_name='my_looks_price_lists')
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, verbose_name='货币')
    date_start = models.DateField('开始日期', default=datetime.today)
    date_end = models.DateField('结束日期', default=datetime.today)

    create_time = models.DateTimeField('创建时间', default=datetime.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['create_time']
        db_table = 'product_looks_price_list'


class AppearanceItemPriceItem(models.Model):
    price_list = models.ForeignKey(AppearanceItemPriceList, on_delete=models.CASCADE, related_name='looks_items_price')

    looks_item = models.ForeignKey(AppearanceItem, on_delete=models.CASCADE, related_name='my_looks_price_items')
    unit_uom = models.ForeignKey(BaseUnit, on_delete=models.CASCADE, verbose_name='单价数量单位')
    rounding = models.CharField('精度', max_length=255, default='0.00')

    mark_price = models.CharField('产品标价(指导售价)', max_length=255, default='0')
    sale_price = models.CharField('销售价格', max_length=255, default='0')
    purchase_price = models.CharField('采购价格', max_length=255, default='0')
    standard_price = models.CharField('成本价格', max_length=255, default='0')

    create_time = models.DateTimeField('创建时间', default=datetime.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return '{} ({})'.format(self.looks_item.name, self.standard_price)

    class Meta:
        ordering = ['create_time']
        db_table = 'product_looks_price_item'


# -----------------------------------------------------------------------------


class ProductParts(models.Model):
    name = models.CharField('配件名称', max_length=255)
    code = models.CharField('编号', max_length=255, default='')
    desc = models.CharField('描述', max_length=255, default='')

    parts_volume = models.CharField('配件体积描述', max_length=255, default='')
    parts_weight = models.CharField('配件重量描述', max_length=255, default='')
    max_available_qty = models.CharField('最大可用数量(1 -- max)', max_length=255, default='1')

    create_time = models.DateTimeField('创建时间', default=datetime.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        db_table = 'product_parts'


class ProductPartsPriceList(models.Model):
    name = models.CharField('配件价格单', max_length=255)
    code = models.CharField('编号', max_length=255, default='')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='所属公司', related_name='my_parts_price_lists')
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, verbose_name='货币')
    date_start = models.DateField('开始日期', default=datetime.today)
    date_end = models.DateField('结束日期', default=datetime.today)

    create_time = models.DateTimeField('创建时间', default=datetime.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['create_time']
        db_table = 'product_parts_price_list'


class ProductPartsPriceItem(models.Model):
    price_list = models.ForeignKey(ProductPartsPriceList, on_delete=models.CASCADE, related_name='parts_price')

    parts = models.ForeignKey(ProductParts, on_delete=models.CASCADE, related_name='parts_items')
    unit_uom = models.ForeignKey(BaseUnit, on_delete=models.CASCADE, verbose_name='单价数量单位')
    rounding = models.CharField('精度', max_length=255, default='0.00')

    mark_price = models.CharField('产品标价(指导售价)', max_length=255, default='0')
    sale_price = models.CharField('销售价格', max_length=255, default='0')
    purchase_price = models.CharField('采购价格', max_length=255, default='0')
    standard_price = models.CharField('成本价格', max_length=255, default='0')

    create_time = models.DateTimeField('创建时间', default=datetime.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return '{} ({})'.format(self.parts.name, self.standard_price)

    class Meta:
        ordering = ['create_time']
        db_table = 'product_parts_price_item'
