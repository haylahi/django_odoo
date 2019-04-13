from datetime import datetime

from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from base.utils import UserProfileManager

"""
文件以文件形式保存
    图片返回 base64
    其他返回文件流

基础模块
    company
    partner
    department
    employee


"""

CHOICES_COMPANY_TYPE = [
    ('PERSONAL', '个人独资企业'),
    ('PARTNER', '合伙企业'),
    ('LLC', '有限责任公司'),
    ('SC', '股份有限公司'),
    ('CROP', '集团公司'),
    ('ORG', '组织'),
    ('UNIT', '单位'),
    ('OTHER', '其他')
]

DEFAULT_COMPANY_TYPE = 'LLC'

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


# ----------------------------------------------------------------------------------------------------------------------


class Company(models.Model):
    """公司"""
    name = models.CharField('公司名称', max_length=255, null=True, blank=True)
    code = models.CharField('唯一编码', max_length=255, null=True, blank=True, unique=True)
    company_type = models.CharField('公司类型', max_length=255, choices=CHOICES_COMPANY_TYPE, default=DEFAULT_COMPANY_TYPE)

    parent_company = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True,
        verbose_name='上级公司', related_name='child_companys'
    )
    # 默认税 默认货币 所在国家 企业统一社会信用代码 营业执照

    uniform_social_credit_code = models.CharField('企业统一社会信用代码(税号)', max_length=255, null=True, blank=True, unique=True)
    legal_person = models.CharField('公司法人', max_length=255, null=True, blank=True)
    default_tax = models.ForeignKey('BaseTax', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='默认税')
    default_currency = models.ForeignKey(
        'Currency', on_delete=models.SET_NULL,
        blank=True, null=True, verbose_name='默认货币'
    )
    country = models.ForeignKey('BaseCountry', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='所在国家')

    create_time = models.DateTimeField('创建时间', default=datetime.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return '{}({})'.format(self.name, self.code)

    def my_child_companies(self):
        return self.child_companys.all()

    class Meta:
        db_table = 'base_company'


class Partner(models.Model):
    """合作伙伴 将公司的信息存入base_partner"""
    company = models.ForeignKey('Company', on_delete=models.CASCADE, null=True, blank=True, verbose_name='所在公司')

    is_customer = models.BooleanField('是否是客户', default=True)
    is_supplier = models.BooleanField('是否是供应商', default=True)

    name = models.CharField('合作伙伴', max_length=255, null=True, blank=True)
    code = models.CharField('唯一编码', max_length=255, null=True, blank=True, unique=True)

    def __str__(self):
        return '{}({})'.format(self.name, self.code)

    class Meta:
        db_table = 'base_partner'


class Department(models.Model):
    """部门"""
    company = models.ForeignKey('Company', on_delete=models.CASCADE, null=True, blank=True, verbose_name='所在公司')
    department_type = models.CharField('部门类型', choices=CHOICES_DEPARTMENT_TYPE,
                                       default=DEFAULT_DEPARTMENT_TYPE, max_length=255)

    parent_department = models.ForeignKey('Department', on_delete=models.SET_NULL,
                                          null=True, blank=True, verbose_name='上级部门', related_name='child_departments')

    name = models.CharField('部门名称', max_length=255, null=True, blank=True)
    code = models.CharField('唯一编码', max_length=255, null=True, blank=True, unique=True)

    def __str__(self):
        return '{}({})'.format(self.name, self.code)

    def my_child_departments(self):
        return self.child_departments.all()

    class Meta:
        db_table = 'base_department'


class Employee(models.Model):
    """员工"""
    company = models.ForeignKey('Company', on_delete=models.CASCADE, null=True, blank=True, verbose_name='所在公司')
    department = models.ForeignKey('Department', on_delete=models.CASCADE, null=True, blank=True, verbose_name='所属部门')
    user = models.ForeignKey('UserProfile', on_delete=models.SET_NULL, verbose_name='uid', null=True, blank=True)

    name = models.CharField('部门名称', max_length=255, null=True, blank=True)
    code = models.CharField('唯一编码', max_length=255, null=True, blank=True, unique=True)

    def __str__(self):
        return '{}({})'.format(self.name, self.code)

    class Meta:
        db_table = 'base_employee'


class UserGroup(models.Model):
    """用户组"""

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
    name = models.CharField('货币', max_length=255, null=True, blank=True)
    code = models.CharField('唯一编码', max_length=255, null=True, blank=True, unique=True)

    class Meta:
        db_table = 'base_unit'


# ----------------------------------------------------------------------------------------------------------------------


class BaseCountry(models.Model):
    name = models.CharField('国家', max_length=255, blank=True, null=True)
    code = models.CharField('唯一编码', max_length=255, null=True, blank=True, unique=True)
    short_name = models.CharField('简称', max_length=255, null=True, blank=True)
    area_code = models.CharField('国家区号', max_length=255, null=True, blank=True, unique=True)
    national_flag = models.CharField('国旗', null=True, blank=True, unique=True, max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'base_country'


class BaseProvince(models.Model):
    country = models.ForeignKey('BaseCountry', on_delete=models.CASCADE, blank=True, null=True, verbose_name='所在国家')
    name = models.CharField('省', max_length=255, blank=True, null=True)
    code = models.CharField('唯一编码', max_length=255, null=True, blank=True, unique=True)
    short_name = models.CharField('简称', max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
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
