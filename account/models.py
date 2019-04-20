from datetime import datetime

from django.db import models

from base.models import Company, Partner

CHOICES_ACCOUNT_TYPE = [
    ('CASH', '现金'),
    ('BANK', '银行'),
    ('WECHAT', '微信'),
    ('ALIPAY', '支付宝'),
    ('CHECK', '支票'),
    ('OTHER', '其他')
]


class AccountAccount(models.Model):
    """
    账号

    内部交易不需要客户 区分收付款

    """
    short_name = models.CharField('账户别名', max_length=255, default='')
    account_type = models.CharField('账户类型', max_length=255, choices=CHOICES_ACCOUNT_TYPE, default='BANK')
    account_name = models.CharField('开户账号', max_length=255)
    account_bank = models.CharField('开户银行', max_length=255)
    account_user = models.CharField('开户名', max_length=255)

    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='所属公司')
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE, verbose_name='所属客户')
    trades_num = models.IntegerField('交易次数', default=0)
    create_time = models.DateTimeField('创建时间', default=datetime.now)
    state = models.CharField('状态', choices=[('DRAFT', '草稿'), ('APPROVE', '待审核'), ('DONE', '完成')], default='DRAFT', max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return '{}[{}]'.format(self.account_name, self.account_bank)

    class Meta:
        ordering = ['-account_bank']
        db_table = 'account_account_bank'


class AccountRecord(models.Model):
    name = models.CharField('收(付)款单号', max_length=255)
    create_time = models.DateTimeField('创建时间', default=datetime.now)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-create_time']
        db_table = 'account_record'
