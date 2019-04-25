from django.db import models


class AccountAccount(models.Model):
    short_name = models.CharField('账户简称', max_length=255)

    account_name = models.CharField('开户名', max_length=255)
    account_bank = models.CharField('开户银行', max_length=255)
    account_card = models.CharField('开户卡号', max_length=255)
