from datetime import datetime
from decimal import Decimal, ROUND_HALF_UP

# noinspection PyUnresolvedReferences
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
# noinspection PyUnresolvedReferences
from django.db.models import (
    Model, CharField, BooleanField, IntegerField,
    DateTimeField, ForeignKey, DateField, AutoField,
    CASCADE, SET_NULL, PROTECT
)

from base.utils import MyUserManager

# -----------------------------------------------------------------------------

"""
Company
Tax
Currency


"""

CHOICES_UNIT_TYPE = [
    ('UNIT', '数量单位'),
    ('TIME', '时间'),
    ('LENGTH', '长度'),
    ('WEIGHT', '重量'),
]

CHOICES_COMPUTE_METHOD = [
    ('std', '相等'),
    ('multi', '乘'),
    ('divide', '除'),
]

DEFAULT_COMPUTE_METHOD = 'std'


# -----------------------------------------------------------------------------


class Province(Model):
    name = CharField('省', max_length=255)
    short_name = CharField('简称', max_length=255)
    is_active = BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class BaseCity(Model):
    province = ForeignKey(Province, on_delete=CASCADE, verbose_name='所在省份', related_name='cities')
    name = CharField('城市', max_length=255)
    area_code = CharField('城市区号', max_length=255)
    is_municipality = BooleanField(default=False, verbose_name='直辖市')
    is_active = BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class BaseUnit(Model):
    name = CharField('单位', max_length=255)
    unit_symbol = CharField('单位符号', max_length=255)
    unit_type = CharField('单位类型', max_length=255, choices=CHOICES_UNIT_TYPE, default='UNIT')
    is_active = BooleanField(default=True)

    is_base_unit = BooleanField('是否为基本单位', default=False)
    rounding = CharField('精度', max_length=255, default='0.00')
    factor = CharField('倍数', max_length=255, default='1')
    compute_method = CharField('计算方式', max_length=255, choices=CHOICES_COMPUTE_METHOD, default=DEFAULT_COMPUTE_METHOD)

    def convert_base_unit(self, val: str):
        """将其他单位转换为标准单位的结果"""
        origin_num = Decimal()
        if self.compute_method == 'std':
            origin_num = Decimal(val)
        if self.compute_method == 'multi':
            origin_num = Decimal(val) * Decimal(self.factor)
        if self.compute_method == 'divide':
            origin_num = Decimal(val) / Decimal(self.factor)
        result_num = origin_num.quantize(Decimal(self.rounding), rounding=ROUND_HALF_UP)
        return str(result_num)

    def __str__(self):
        return '{}{} ({})'.format(self.name, self.unit_symbol, self.get_unit_type_display())

    class Meta:
        unique_together = ('unit_type', 'is_base_unit')
        ordering = ['unit_type', 'name']


class Sequence(Model):
    """
    序列号规则
    TODO 生成下一个序列号

    """
    name = CharField('序列号名称', max_length=255)
    code = CharField('指定编码', max_length=255, unique=True)

    padding = IntegerField('填充长度', default=5)
    step_len = IntegerField('步长', default=1)
    next_number = IntegerField('下个序列号', default=1)

    suffix = CharField('后缀', max_length=255, default='')
    prefix = CharField('前缀', max_length=255, default='')
    create_time = DateTimeField('创建时间', default=datetime.now)
    is_active = BooleanField(default=True)

    def __str__(self):
        return '{} [{}]'.format(self.name, self.code)

    class Meta:
        ordering = ['name']


# -----------------------------------------------------------------------------

class Partner(Model):
    name = CharField('合作伙伴名称', max_length=255)
    code = CharField('Code', max_length=255, default='')
    description = CharField('描述', max_length=255, default='')

    create_time = DateTimeField('创建时间', default=datetime.now)
    is_active = BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Company(Model):
    name = CharField('Company', max_length=255)
    code = CharField('Code', max_length=255, default='')
    description = CharField('描述', max_length=255, default='')
    website = CharField('公司网址', max_length=255, default='')
    email = CharField('公司邮箱', max_length=255, default='')

    province = ForeignKey(Province, on_delete=SET_NULL, null=True, blank=True, verbose_name='省份')
    city = ForeignKey(BaseCity, on_delete=SET_NULL, null=True, blank=True, verbose_name='城市')
    address = CharField('详细地址', max_length=255, default='')

    create_time = DateTimeField('创建时间', default=datetime.now)
    is_active = BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name', '-create_time']


class Department(Model):
    company = ForeignKey(Company, on_delete=CASCADE, verbose_name='所在公司', related_name='company_departments')
    name = CharField('部门名称', max_length=255)
    code = CharField('Code', max_length=255, default='')

    create_time = DateTimeField('创建时间', default=datetime.now)
    is_active = BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class BaseJob(Model):
    """
    职位
    职位类别 管理 技术 。。。  职位技能需求
    """
    name = CharField('职称', max_length=255)
    code = CharField('Code', max_length=255, default='')

    create_time = DateTimeField('创建时间', default=datetime.now)
    is_active = BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class BaseUser(AbstractBaseUser, PermissionsMixin):
    """
    BaseUser

    """
    company = ForeignKey(Company, on_delete=CASCADE, null=True, blank=True, verbose_name='所属公司', related_name='company_users')
    department = ForeignKey(Department, on_delete=CASCADE, null=True, blank=True, verbose_name='所属部门', related_name='department_users')
    # 当职位下还有用户时不能删除
    job = ForeignKey(BaseJob, on_delete=PROTECT, null=True, blank=True, verbose_name='职称')

    username = CharField('username', max_length=255, unique=True, validators=[UnicodeUsernameValidator()])
    email = CharField('email', max_length=255, default='')
    is_staff = BooleanField('staff', default=True)

    create_time = DateTimeField('创建时间', default=datetime.now)
    is_active = BooleanField(default=True)

    # ################## 个人信息 #####################

    # ################## 工作信息 #####################
    is_department_manager = BooleanField(default=False, verbose_name='部门经理')

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    objects = MyUserManager()

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['username', '-create_time']


# -----------------------------------------------------------------------------


class UserOperationLog(Model):
    user = ForeignKey(BaseUser, on_delete=CASCADE, verbose_name='所属用户', related_name='user_op_logs')
    app_name = CharField('所在app名称', max_length=255)
    model_name = CharField('操作的模型', max_length=255)
    model_id = CharField('操作模型的id', max_length=255)
    content = CharField('操作内容', max_length=255, default='')
    result = CharField('操作结果', max_length=255, default='')

    create_time = DateTimeField('创建时间', default=datetime.now)
    is_active = BooleanField(default=True)

    def __str__(self):
        return '{}--{}({})'.format(self.user, self.model_name, self.model_id)

    class Meta:
        ordering = ['-create_time']


class FileObject(Model):
    """
    一个文件附件就是一个文件对象
    开启开关 --> can_upload_file
    """
    app_label = CharField('所属APP', max_length=255, default='')
    model_name = CharField('所属模型', max_length=255, default='')
    # 适用与某个对象的字段 如图片字段取最新字段 或者把 值赋给 对象的字段中去
    model_field = CharField('所属字段', max_length=255, default='')
    model_id = CharField('所属对象ID', max_length=255, default='')

    file_name = CharField('原始文件名', max_length=255)
    file_suffix = CharField('文件后缀名', max_length=255, default='.txt', help_text='保存形式为 xxx.txt')
    file_path = CharField('文件相对路径', max_length=255, unique=True)
    file_coding = CharField('文件编码格式', max_length=255, default='utf8')
    file_type = CharField('文件类型', max_length=255, default='')

    create_time = DateTimeField('创建时间', default=datetime.now)
    is_active = BooleanField(default=True)

    # -------------------------------------------------------------------------

    def __str__(self):
        return self.file_name

    class Meta:
        ordering = ['-create_time']
