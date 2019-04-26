from datetime import datetime

from django.contrib.auth import get_user_model
from django.db import models

from base.models import Company, Partner

User = get_user_model()

CHOICES_ACCOUNT_TYPE = [
    ('bank', '银行账户'),
    ('wechat', '微信'),
    ('alipay', '支付宝'),
    ('cash', '现金'),
]

DEFAULT_ACCOUNT_TYPE = 'bank'

CHOICES_USAGE_TYPE = [
    ('partner', '客户'),
    ('employee', '员工'),
]


class AccountAccount(models.Model):
    short_name = models.CharField('账户简称', max_length=255)
    account_type = models.CharField('账户类型', max_length=255, choices=CHOICES_ACCOUNT_TYPE, default=DEFAULT_ACCOUNT_TYPE)
    usage_type = models.CharField('使用类型', max_length=255, choices=CHOICES_USAGE_TYPE, default='partner')
    # 该账户信息只能被该公司看到
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='所属公司')

    account_name = models.CharField('开户名', max_length=255)
    account_bank = models.CharField('开户银行', max_length=255)
    account_card = models.CharField('开户卡号', max_length=255)
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE, verbose_name='归属客户', null=True, blank=True)

    belongs_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='所属员工', related_name='account_belongs_user')
    create_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='创建用户', related_name='account_create_user')
    create_time = models.DateTimeField('创建时间', default=datetime.now)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return '{} [{}]'.format(self.short_name, self.account_card)

    class Meta:
        ordering = ['account_card']
