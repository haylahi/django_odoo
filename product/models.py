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
解析excel数据


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
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='所属用户', related_name='user_product_tags')

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
    product_image = models.ImageField(verbose_name='产品图片', upload_to='product_image/', storage=CustomFileStorage(), default='default_logo.png')

    brand = models.ForeignKey(ProductBrand, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='所属品牌')
    category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='所属类别')
    tags = models.ManyToManyField(ProductTag, verbose_name='标签', blank=True)

    # 排序算法 ...
    product_display_rank = models.CharField('产品显示排序', default='', max_length=255)
    is_dummy_special_product = models.BooleanField('特殊定制？(虚拟)', default=False)

    product_type = models.CharField('产品属性', max_length=255, choices=CHOICES_PRODUCT_TYPE, default='STD')
    product_usage_type = models.CharField('产品销售属性', max_length=255, choices=CHOICES_PRODUCT_USAGE_TYPE, default='NORMAL')

    # 订单的默认来源数量单位
    default_unit_uom = models.ForeignKey(
        BaseUnit, verbose_name='默认数量单位',
        on_delete=models.SET_NULL, null=True, blank=True, related_name='product_unit_uom_list'
    )

    default_volume_uom = models.ForeignKey(
        BaseUnit, verbose_name='默认体积单位',
        on_delete=models.SET_NULL, null=True, blank=True, related_name='product_volume_uom_list'
    )
    product_length = models.CharField('产品(长)', max_length=255, default='')
    product_width = models.CharField('产品(宽)', max_length=255, default='')
    product_height = models.CharField('产品(高)', max_length=255, default='')

    can_sale = models.BooleanField('可以销售？', default=True)
    can_purchase = models.BooleanField('可以采购？', default=True)
    use_stock = models.BooleanField('使用库存？', default=True)
    stock_tracking = models.CharField('产品库存追踪', max_length=255, choices=CHOICES_STOCK_TRACKING, default='LOT')

    #  条码唯一性验证
    barcode = models.CharField('商品条码', max_length=255, default='')
    create_time = models.DateTimeField('创建时间', default=datetime.now)
    is_active = models.BooleanField(default=True)

    """
    产品属性分类  服务类 虚拟类 配件类
    产品外观   体积  重量  
    产品可以使用属性 可生产 可售 停产 等等...
    产品价格表  子公司可以看到的产品列表

    """

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
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='所属公司')
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
    price_list = models.ForeignKey(ProductPriceList, on_delete=models.CASCADE, verbose_name='产品价格单')
    # 产品价格表 图表
    product = models.ForeignKey(ProductProduct, on_delete=models.CASCADE, verbose_name='产品', related_name='product_price_list')
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


# -------------------------------------------------------------------------------------------------


class PartsGroup(models.Model):
    name = models.CharField('配件组', max_length=255)
    code = models.CharField('编号', max_length=255, default='')
    desc = models.CharField('描述', max_length=255, default='')
    create_time = models.DateTimeField('创建时间', default=datetime.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-name']
        db_table = 'product_parts_group'


class PartsInfo(models.Model):
    group = models.ForeignKey(PartsGroup, on_delete=models.CASCADE, verbose_name='配件组')

    name = models.CharField('配件', max_length=255)
    code = models.CharField('编号', max_length=255, default='')
    desc = models.CharField('描述', max_length=255, default='')
    max_available_qty = models.CharField('最大可用数量', default='1',max_length=255)
    product = models.ForeignKey('ProductProduct', on_delete=models.CASCADE, verbose_name='所属产品', related_name='product_parts_list')
    default_looks = models.ForeignKey('LooksInfo', on_delete=models.SET_NULL, verbose_name='默认外观', null=True, blank=True)
    # 过滤
    parts_uom = models.ForeignKey(BaseUnit, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='配件默认数量单位')
    create_time = models.DateTimeField('创建时间', default=datetime.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-name']
        db_table = 'product_parts_info'


class LooksGroup(models.Model):
    """
    空白色板组
    """
    name = models.CharField('外观组', max_length=255)
    code = models.CharField('编号', max_length=255, default='')
    desc = models.CharField('描述', max_length=255, default='')

    create_time = models.DateTimeField('创建时间', default=datetime.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-name']
        db_table = 'product_looks_group'


class LooksInfo(models.Model):
    group = models.ForeignKey(LooksGroup, on_delete=models.CASCADE, verbose_name='外观组')
    name = models.CharField('外观', max_length=255)
    code = models.CharField('编号', max_length=255, default='')
    desc = models.CharField('描述', max_length=255, default='')

    create_time = models.DateTimeField('创建时间', default=datetime.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-name']
        db_table = 'product_looks_info'


class PartsLooksMap(models.Model):
    """
    配件外观选配 包括主产品的外观
    当只选择了产品 则产品下面的所有配件都有色板可选配
    过滤条件  选配组类型为 色板的选配部件才可以 选配
    """
    name = models.CharField('选配名称', max_length=255, default='')

    # 为产品所有的配件增加选配信息
    parts_info = models.ForeignKey(PartsInfo, on_delete=models.CASCADE, null=True, blank=True, verbose_name='配件范围')

    # 色板 色板组 二选一  /
    looks_group = models.ForeignKey(LooksGroup, on_delete=models.CASCADE, null=True, blank=True, verbose_name='色板组')
    looks_info = models.ForeignKey(
        LooksInfo, on_delete=models.CASCADE,
        null=True, blank=True, verbose_name='色板', related_name='map_looks_list'
    )
    exclude_looks_info = models.ForeignKey(
        LooksInfo, on_delete=models.CASCADE,
        null=True, blank=True, verbose_name='例外色板', related_name='map_exclude_looks_list'
    )
    create_time = models.DateTimeField('创建时间', default=datetime.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['create_time']
        db_table = 'product_parts_looks_map'


class PartsLooksPriceList(models.Model):
    name = models.CharField('选配定价单', max_length=255, default='')
    code = models.CharField('编号', max_length=255, default='')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='所属公司')
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, verbose_name='货币')

    unit_uom = models.ForeignKey(BaseUnit, on_delete=models.CASCADE, verbose_name='单价数量单位')
    parts = models.ForeignKey(PartsInfo, on_delete=models.CASCADE, verbose_name='所属配件')

    date_start = models.DateField('开始日期', default=datetime.today)
    date_end = models.DateField('结束日期', default=datetime.today)
    create_time = models.DateTimeField('创建时间', default=datetime.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['create_time']
        db_table = 'prats_looks_price_list'


class PartsLooksPriceItem(models.Model):
    price_list = models.ForeignKey(PartsLooksPriceList, on_delete=models.CASCADE, verbose_name='价格单')

    # 色板 色板组 二选一  /
    looks_group = models.ForeignKey(LooksGroup, on_delete=models.CASCADE, null=True, blank=True, verbose_name='色板组')
    looks_info = models.ForeignKey(LooksInfo, on_delete=models.CASCADE, null=True, blank=True, verbose_name='色板')

    mark_price = models.CharField('产品标价(指导售价)', max_length=255, default='0')
    sale_price = models.CharField('销售价格', max_length=255, default='0')
    purchase_price = models.CharField('采购价格', max_length=255, default='0')
    standard_price = models.CharField('成本价格', max_length=255, default='0')

    create_time = models.DateTimeField('创建时间', default=datetime.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.mark_price

    class Meta:
        ordering = ['create_time']
        db_table = 'prats_looks_price_item'


# -----------------------------------------------------------------------------


class ProductPacking(models.Model):
    """用于存放选配后的产品 以便于以后快速选择 比如热销款式"""
    name = models.CharField('包装名称', max_length=255)
    code = models.CharField('编号', max_length=255, default='')
    desc = models.CharField("选配描述", max_length=255)

    pack_qty = models.CharField('套装数量', max_length=255, default='1')
    pack_uom = models.ForeignKey(
        BaseUnit, on_delete=models.SET_NULL, verbose_name='包装默认单位',
        null=True, blank=True, related_name='packing_pack_uom_list'
    )

    product = models.ForeignKey(ProductProduct, on_delete=models.CASCADE, verbose_name='主产品')
    product_uom = models.ForeignKey(
        BaseUnit, on_delete=models.SET_NULL, null=True, blank=True,
        verbose_name='产品单位', related_name='packing_product_uom_list'
    )
    product_qty = models.CharField('当前单位数量', max_length=255, default='1')

    create_time = models.DateTimeField('创建时间', default=datetime.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def generate_special_code(self):
        """生成特殊编码 用于验证一个选配是否与之相同"""
        pass

    class Meta:
        ordering = ['create_time']
        db_table = 'product_packing'


class ProductPackingList(models.Model):
    packing = models.ForeignKey(ProductPacking, on_delete=models.CASCADE, related_name='packing_list')

    parts = models.ForeignKey(PartsInfo, on_delete=models.CASCADE, verbose_name='配件')
    parts_uom = models.ForeignKey(BaseUnit, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='配件单位')
    parts_qty = models.CharField('配件数量', max_length=255, default='1')
    looks_info = models.ForeignKey(LooksInfo, on_delete=models.CASCADE, verbose_name='配件色板')

    create_time = models.DateTimeField('创建时间', default=datetime.now)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['create_time']
        db_table = 'product_packing_list'
