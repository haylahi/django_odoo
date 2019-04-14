from datetime import datetime

from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from .utils import UserProfileManager, CustomFileStorage, compute_float

"""
文件以文件形式保存
    图片返回 base64
    其他返回文件流

基础模块
    company
    partner
    department
    employee
    
    银行账号 支付宝 现金 银行卡 微信


"""

CHOICES_SEX = [
    ('MALE', '男'),
    ('FEMALE', '女'),
    ('NULL', '未知'),
]

DEFAULT_SEX = 'NULL'

CHOICES_DEPARTMENT_TYPE = [
    ('NORMAL', '常规'),
    ('SPECIAL', '特殊'),
    ('STORE', '子公司门店'),
    ('OTHER', '其他'),
]

DEFAULT_DEPARTMENT_TYPE = 'NORMAL'

CHOICES_UNIT_TYPE = [
    ('UNIT', '数量单位'),
    ('WEIGHT', '质量'),
    ('TIME', '时间'),
    ('LENGTH', '长度'),
    ('OTHER', '其他')
]

DEFAULT_UNIT_TYPE = 'UNIT'

CHOICES_COMPUTE_TYPE = [
    ('STD', '标准'),
    ('RIDE', '大于'),
    ('DIVIDE', '小于'),
]

DEFAULT_COMPUTE_TYPE = 'STD'
COMPUTE_TYPE_BIGGER = 'RIDE'
COMPUTE_TYPE_SMALLER = 'DIVIDE'


# ----------------------------------------------------------------------------------------------------------------------


class Company(models.Model):
    """公司"""
    name = models.CharField('公司名称', max_length=255, null=True, blank=True)
    code = models.CharField('唯一编码', max_length=255, null=True, blank=True, unique=True)
    parent_company = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True,
        verbose_name='上级公司', related_name='child_companys'
    )

    default_tax = models.ForeignKey('BaseTax', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='默认税')
    default_currency = models.ForeignKey(
        'Currency', on_delete=models.SET_NULL,
        blank=True, null=True, verbose_name='默认货币'
    )

    child_dummy_balance = models.CharField('返点资金余额', max_length=255, default='0')
    child_cash_balance = models.CharField('实际资金余额', max_length=255, default='0')
    dummy_discount = models.CharField('默认返点比例(%)', max_length=255, default='40')

    create_time = models.DateTimeField('创建时间', default=datetime.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return '{}({})'.format(self.name, self.code)

    def my_child_companies(self):
        return self.child_companys.all()

    class Meta:
        ordering = ['-name']
        db_table = 'base_company'


class PartnerTag(models.Model):
    name = models.CharField('名称', max_length=255, unique=True)
    color = models.CharField('颜色', max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'base_partner_tag'


class Partner(models.Model):
    """合作伙伴 将公司的信息存入base_partner 可以是个人或者公司"""
    company = models.ForeignKey('Company', on_delete=models.CASCADE, null=True, blank=True, verbose_name='所在公司')
    name = models.CharField('合作伙伴', max_length=255, null=True, blank=True)
    code = models.CharField('唯一编码', max_length=255, null=True, blank=True, unique=True)
    desc = models.CharField('详细描述', max_length=255, null=True, blank=True)

    is_customer = models.BooleanField('是否是客户', default=True)
    is_supplier = models.BooleanField('是否是供应商', default=True)

    partner_tags = models.ManyToManyField('PartnerTag', blank=True, verbose_name='标签')

    # 详细信息
    uniform_social_credit_code = models.CharField('企业统一社会信用代码(税号)', max_length=255, null=True, blank=True, unique=True)
    legal_person = models.CharField('公司法人', max_length=255, null=True, blank=True)
    register_date = models.DateField('成立时间', null=True, blank=True)

    logo = models.ImageField(
        '公司Logo', upload_to='company_logo/',
        storage=CustomFileStorage(), null=True, blank=True, unique=True
    )
    web_site = models.URLField('合作伙伴网址', max_length=255, null=True, blank=True)
    contact_info = models.CharField('联系方式', max_length=255, null=True, blank=True)
    email = models.EmailField('合作伙伴邮箱', max_length=255, null=True, blank=True)

    # 地址信息
    country = models.ForeignKey('BaseCountry', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='所在国家')
    province = models.ForeignKey('BaseProvince', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='省份')
    city = models.ForeignKey('BaseCity', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='城市')
    address = models.CharField('详细地址', max_length=255, null=True, blank=True)

    # TODO 仓库位置 指定一个虚拟虚拟位置 银行账户 客户类型

    def __str__(self):
        return '{}({})'.format(self.name, self.code)

    class Meta:
        db_table = 'base_partner'


class Department(models.Model):
    """部门"""
    company = models.ForeignKey('Company', on_delete=models.CASCADE, null=True, blank=True, verbose_name='所在公司')
    name = models.CharField('部门名称', max_length=255, null=True, blank=True)
    code = models.CharField('唯一编码', max_length=255, null=True, blank=True, unique=True)
    desc = models.CharField('详细描述', max_length=255, null=True, blank=True)
    logo = models.ImageField(
        '部门Logo', upload_to='department_logo/',
        storage=CustomFileStorage(), null=True, blank=True, unique=True
    )

    department_type = models.CharField(
        '部门类型', max_length=255,
        choices=CHOICES_DEPARTMENT_TYPE, default=DEFAULT_DEPARTMENT_TYPE
    )

    parent_department = models.ForeignKey(
        'Department', on_delete=models.SET_NULL,
        null=True, blank=True, verbose_name='上级部门',
        related_name='child_departments'
    )

    def __str__(self):
        return '{}({})'.format(self.name, self.code)

    def my_child_departments(self):
        return self.child_departments.all()

    def department_manager(self):
        employees = self.employees.all().filter(is_active=True, is_department_manager=True)
        if employees and len(employees) == 1:
            return employees[0]
        else:
            return None

    class Meta:
        db_table = 'base_department'


class JobClassification(models.Model):
    name = models.CharField('职位名称', max_length=255)
    code = models.CharField('唯一编码', max_length=255, null=True, blank=True, unique=True)
    desc = models.CharField('详细描述', max_length=255, null=True, blank=True)
    requirement = models.CharField('技能要求', max_length=255, null=True, blank=True)

    pub_date = models.DateField('发布日期', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'base_job'


class Employee(models.Model):
    """员工"""
    company = models.ForeignKey('Company', on_delete=models.CASCADE, null=True, blank=True, verbose_name='所在公司')
    department = models.ForeignKey(
        'Department', on_delete=models.CASCADE,
        null=True, blank=True, verbose_name='所属部门', related_name='employees'
    )
    user = models.ForeignKey('UserProfile', on_delete=models.SET_NULL, verbose_name='uid', null=True, blank=True)
    job = models.ForeignKey('JobClassification', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='职位')
    is_department_manager = models.BooleanField(default=False, verbose_name='部门经理')

    name = models.CharField('部门名称', max_length=255, null=True, blank=True)
    code = models.CharField('工号', max_length=255, null=True, blank=True, unique=True)

    work_address = models.CharField('工作地址', max_length=255, null=True, blank=True)
    work_email = models.CharField('工作邮箱', max_length=255, null=True, blank=True)
    work_contact = models.CharField('工作联系方式', max_length=255, null=True, blank=True)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return '{}({})'.format(self.name, self.code)

    def my_department_manager(self):
        return self.department.department_manager()

    class Meta:
        db_table = 'base_employee'


class UserGroup(models.Model):
    """用户组"""
    name = models.CharField('用户组名', max_length=255, null=True, blank=True)
    code = models.CharField('唯一编码', max_length=255, null=True, blank=True, unique=True)
    parent = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True,
        verbose_name='上级用户组', related_name='child_groups'
    )
    users = models.ManyToManyField('UserProfile', blank=True)
    create_time = models.DateTimeField('创建时间', default=datetime.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def my_child_groups(self):
        return self.child_groups.all()

    class Meta:
        db_table = 'base_user_group'


class UserProfile(AbstractBaseUser):
    company = models.ForeignKey('Company', on_delete=models.CASCADE, null=True, blank=True, verbose_name='所在公司')

    email = models.EmailField(verbose_name='Email', max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    create_time = models.DateTimeField('创建时间', default=datetime.now)

    # ----------- function
    objects = UserProfileManager()

    USERNAME_FIELD = 'email'

    def create_user_info(self):
        return UserInfo.objects.create(user=self, create_time=self.create_time)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return True

    def __str__(self):
        return self.email

    class Meta:
        ordering = ['-create_time']
        db_table = 'base_user'


class UserInfo(models.Model):
    user = models.ForeignKey('UserProfile', on_delete=models.CASCADE, verbose_name='uid')

    real_name = models.CharField('姓名', max_length=255, null=True, blank=True)
    nickname = models.CharField('昵称', max_length=255, null=True, blank=True)
    sex = models.CharField('性别', max_length=255, choices=CHOICES_SEX, default=DEFAULT_SEX)

    create_time = models.DateTimeField('创建时间', default=datetime.now)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'base_user_info'


class BaseTax(models.Model):
    name = models.CharField('税', max_length=255, null=True, blank=True)
    code = models.CharField('唯一编码', max_length=255, null=True, blank=True, unique=True)

    class Meta:
        db_table = 'base_tax'


class Currency(models.Model):
    name = models.CharField('货币', max_length=255, null=True, blank=True)
    code = models.CharField('唯一编码', max_length=255, null=True, blank=True, unique=True)

    class Meta:
        db_table = 'base_currency'


class BaseUnit(models.Model):
    name = models.CharField('单位', max_length=255, null=True, blank=True)
    code = models.CharField('唯一编码', max_length=255, null=True, blank=True, unique=True)
    unit_type = models.CharField('单位类别', max_length=255, choices=CHOICES_UNIT_TYPE, default=DEFAULT_UNIT_TYPE)
    factor = models.CharField('比例', max_length=255, default='1')
    rounding = models.CharField('精度', max_length=255, default='0.00')
    compute_type = models.CharField('计算方式', max_length=255, choices=CHOICES_COMPUTE_TYPE, default=DEFAULT_COMPUTE_TYPE)

    def __str__(self):
        if self.code:
            return '{}({})'.format(self.name, self.code)
        return self.name

    def convert2standard(self, number: str) -> str:
        try:
            float(number)
            float(self.rounding)
        except:
            raise ValueError('[ERROR] convert str to float error')
        if self.compute_type == DEFAULT_COMPUTE_TYPE:
            return compute_float(number, self.rounding)

        elif self.compute_type == COMPUTE_TYPE_BIGGER:
            _num = float(number) * float(self.factor)
            return compute_float(str(_num), self.rounding)

        elif self.compute_type == COMPUTE_TYPE_SMALLER:
            _num = float(number) / float(self.factor)
            return compute_float(str(_num), self.rounding)

    class Meta:
        ordering = ['-name']
        db_table = 'base_unit'


# ----------------------------------------------------------------------------------------------------------------------


class BaseCountry(models.Model):
    name = models.CharField('国家', max_length=255, blank=True, null=True)
    code = models.CharField('唯一编码', max_length=255, null=True, blank=True, unique=True)
    short_name = models.CharField('简称', max_length=255, null=True, blank=True)
    area_code = models.CharField('国家区号', max_length=255, null=True, blank=True, unique=True)

    national_flag = models.ImageField(
        '国旗图标', upload_to='country_image/',
        default='country_image/national_flag.png',
        storage=CustomFileStorage(), null=True, blank=True, unique=True
    )
    create_time = models.DateTimeField('创建时间', default=datetime.now)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-name']
        db_table = 'base_country'


class BaseProvince(models.Model):
    country = models.ForeignKey('BaseCountry', on_delete=models.CASCADE, blank=True, null=True, verbose_name='所在国家')
    name = models.CharField('省', max_length=255, blank=True, null=True)
    code = models.CharField('唯一编码', max_length=255, null=True, blank=True, unique=True)
    short_name = models.CharField('简称', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-name']
        db_table = 'base_province'


class BaseCity(models.Model):
    """
    电话区号 车牌号
    """
    province = models.ForeignKey('BaseProvince', on_delete=models.CASCADE, blank=True, null=True, verbose_name='所在省份')
    name = models.CharField('城市', max_length=255, blank=True, null=True)
    code = models.CharField('唯一编码', max_length=255, null=True, blank=True, unique=True)
    area_code = models.CharField('城市区号', max_length=255, null=True, blank=True, unique=True)
    car_number = models.CharField('车牌号首字母', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'base_city'


class BaseDistrict(models.Model):
    """区"""
    city = models.ForeignKey('BaseCity', on_delete=models.CASCADE, blank=True, null=True, verbose_name='所在城市')
    name = models.CharField('区', max_length=255, null=True, blank=True)
    code = models.CharField('唯一编码', max_length=255, null=True, blank=True, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'base_district'
