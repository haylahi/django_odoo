from datetime import datetime
from decimal import Decimal, ROUND_HALF_UP

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
# models
from django.db.models import (
    Model, CharField, BooleanField,
    DateTimeField, ForeignKey, CASCADE, SET_NULL
)
# -----------------------------------------------------------------------------
from django.db.models.signals import post_save
from django.dispatch import receiver

from base.utils import MyUserManager

"""
Company



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


# -----------------------------------------------------------------------------


class Province(Model):
    name = CharField('省', max_length=255)
    short_name = CharField('简称', max_length=255)
    is_active = BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        db_table = 'base_province'


class BaseCity(Model):
    province = ForeignKey(Province, on_delete=CASCADE, verbose_name='所在省份', related_name='cities')
    name = CharField('城市', max_length=255)
    area_code = CharField('城市区号', max_length=255)
    is_active = BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        db_table = 'base_city'


class BaseUnit(Model):
    name = CharField('单位', max_length=255)
    unit_symbol = CharField('单位符号', max_length=255)
    unit_type = CharField('单位类型', max_length=255, choices=CHOICES_UNIT_TYPE, default='UNIT')
    is_active = BooleanField(default=True)

    is_base_unit = BooleanField('是否为基本单位', default=False)
    rounding = CharField('精度', max_length=255, default='0.00')
    factor = CharField('倍数', max_length=255, default='1')
    compute_method = CharField('计算方式', max_length=255, choices=CHOICES_COMPUTE_METHOD, default='std')

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
        db_table = 'base_unit'


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
        db_table = 'base_company'


class BaseUser(AbstractBaseUser, PermissionsMixin):
    """
    BaseUser
    TODO 重新设计用户的 Groups

    """
    company = ForeignKey(Company, on_delete=CASCADE, null=True, blank=True, verbose_name='所属公司')

    username = CharField('username', max_length=255, unique=True, validators=[UnicodeUsernameValidator()])
    email = CharField('email', max_length=255, default='')
    is_staff = BooleanField('staff', default=True)

    create_time = DateTimeField('创建时间', default=datetime.now)
    is_active = BooleanField(default=True)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    objects = MyUserManager()

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['-create_time']
        db_table = 'base_user'


@receiver(post_save, sender=BaseUser)
def user_post_save(sender, **kwargs):
    """
    用户创建之后
    :param sender: BaseUser
    :param kwargs: created : 是否创建成功  instance: 当前实例
    """
    from django.conf import settings

    user, created = kwargs['instance'], kwargs['created']
    if created and user.username != settings.ANONYMOUS_USER_NAME:
        print('xxxxx')
