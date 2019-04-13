from datetime import datetime

from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db import models

"""
基础模块
    company


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
    create_time = models.DateTimeField('创建时间', default=datetime.now)

    def __str__(self):
        return '{}[{}]'.format(self.name, self.code)

    class Meta:
        db_table = 'base_company'


class Partner(models.Model):
    """合作伙伴 将公司的信息存入base_partner"""
    company = models.ForeignKey('Company', on_delete=models.CASCADE, null=True, blank=True, verbose_name='所在公司')

    name = models.CharField('合作伙伴', max_length=255, null=True, blank=True)
    code = models.CharField('唯一编码', max_length=255, null=True, blank=True, unique=True)

    def __str__(self):
        return '{}[{}]'.format(self.name, self.code)

    class Meta:
        db_table = 'base_partner'


class UserProfileManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        user.create_user_info()
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user


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
        return UserInfo.objects.create(user=self)

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
