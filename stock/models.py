from datetime import datetime

from django.db import models

from base.models import Company, BaseSequence, Partner
from base.utils import CHOICES_STATE, DEFAULT_STATE

# TODO 物流  物流单号 审核人 审核日期 包装区分不同的产品

CHOICES_LOCATION_TYPE = [
    ('VIEW', '视图位置'),
    ('INTERNAL', '内部位置'),
    ('SUPPLIER', '供应商位置'),
    ('CUSTOMER', '客户位置'),
    ('PRODUCTION', '生产位置'),
]

DEFAULT_LOCATION_TYPE = 'INTERNAL'

CHOICES_OP_TYPE = [
    ('INBOUND', '供应商'),
    ('OUTBOUND', '客户'),
    ('INTERNAL', '内部'),
]

DEFAULT_OP_TYPE = 'INTERNAL'

# C子公司  P父级公司  U客户  T F R
CHOICES_DIFF_TYPE = [
    ('PFU', '总公司从供应商收货'),  # 采购
    ('PTC', '总公司对子公司发货'),  # 销售
    ('PTU', '总公司对客户发货'),  # 销售
    ('PRU', '总公司对供应商退货'),
    ('CFP', '子公司从总公司收货'),  # 采购 经销商收货单
    ('CFU', '子公司从供应商收货'),  # 采购
    ('CTU', '子公司对客户发货'),  # 经销商发货单
    ('CRU', '子公司对供应商退货'),
    ('CRP', '子公司对总公司退货'),  # 经销商退货单
    ('URP', '客户对总公司退货'),
    ('URC', '客户对子公司退货')  # 终端退货单
]


# ---------------------------------------------------------------------------------------------------------------------


class StockWarehouse(models.Model):
    name = models.CharField('仓库名称', max_length=255, default='')
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
    name = models.CharField('仓库名称', max_length=255, default='')
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


class StockPickingType(models.Model):
    """根据 仓库 diff_type"""
    name = models.CharField('作业类型', max_length=255)
    code = models.CharField('唯一编码', max_length=255, unique=True)
    short_name = models.CharField('简称', max_length=255, null=True, blank=True)
    address = models.CharField('仓库位置地址', max_length=255, null=True, blank=True)
    create_time = models.DateTimeField('创建时间', default=datetime.now)
    is_active = models.BooleanField(default=True)

    diff_type = models.CharField('区分作业类型', max_length=255, choices=CHOICES_DIFF_TYPE, default='CFP')

    warehouse = models.ForeignKey('StockWarehouse', on_delete=models.CASCADE, null=True, blank=True, verbose_name='所属仓库')
    sequence = models.ForeignKey(BaseSequence, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='序列号')
    op_type = models.CharField('出入站类型', max_length=255, choices=CHOICES_OP_TYPE, default=DEFAULT_OP_TYPE)
    return_picking_type = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='退回的作业类型')

    show_reserved = models.BooleanField('显示预留', default=False)
    use_new_lot = models.BooleanField('是否创建新的批次号', default=False)
    use_already_lot = models.BooleanField('是否使用已有的批次号', default=False)
    default_source_location = models.ForeignKey('StockLocation', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='默认来源位置', related_name='default_source_locations')
    default_destination_location = models.ForeignKey('StockLocation', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='默认目的位置', related_name='default_destination_locations')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-name']
        db_table = 'stock_picking_type'


class StockPicking(models.Model):
    """
    库存调拨

    采购单 ID  销售单ID

    """
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True, verbose_name='所在公司')
    name = models.CharField('库存调拨单号', max_length=255, unique=True, default='stock_picking')
    origin = models.CharField('源单据号', max_length=255, null=True, blank=True)
    note = models.CharField('备注', max_length=255, null=True, blank=True)

    from_contact = models.CharField('源位置联系方式', max_length=255, null=True, blank=True)
    to_contact = models.CharField('目的位置联系方式', max_length=255, null=True, blank=True)
    return_note = models.CharField('退货原因', max_length=255, null=True, blank=True)
    real_price_total = models.CharField('实际含税金额', max_length=255, null=True, blank=True)
    purchase_order_id = models.CharField('采购单ID', max_length=255, null=True, blank=True)
    sale_order_id = models.CharField('销售单ID', max_length=255, null=True, blank=True)
    picking_diff_type = models.CharField('作业类型特殊编码', max_length=255, null=True, blank=True)

    partner = models.ForeignKey(Partner, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='合作伙伴')
    picking_type = models.ForeignKey('StockPickingType', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='作业类型')
    source_location = models.ForeignKey('StockLocation', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='来源位置', related_name='source_locations')
    destination_location = models.ForeignKey('StockLocation', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='目的位置', related_name='destination_locations')

    create_time = models.DateTimeField('创建时间', default=datetime.now)
    create_date = models.DateField('创建日期', default=datetime.today)
    expect_date = models.DateField('预计完成日期', null=True, blank=True)
    done_date = models.DateField('完成日期', null=True, blank=True)
    state = models.CharField('状态', max_length=255, choices=CHOICES_STATE, default=DEFAULT_STATE)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-create_time', '-name']
        db_table = 'stock_picking'


class StockMove(models.Model):
    class Meta:
        db_table = 'stock_move'


class StockMoveLine(models.Model):
    class Meta:
        db_table = 'stock_move_line'


class StockProductionLot(models.Model):
    class Meta:
        db_table = 'stock_production_lot'


class StockQuantity(models.Model):
    class Meta:
        db_table = 'stock_quant'
