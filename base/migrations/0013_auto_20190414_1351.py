# Generated by Django 2.0.4 on 2019-04-14 13:51

import base.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_partner_register_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='desc',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='详细描述'),
        ),
        migrations.AddField(
            model_name='department',
            name='logo',
            field=models.ImageField(blank=True, null=True, storage=base.utils.CustomFileStorage(), unique=True, upload_to='department_logo/', verbose_name='部门Logo'),
        ),
        migrations.AddField(
            model_name='employee',
            name='is_department_manager',
            field=models.BooleanField(default=False, verbose_name='部门经理'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='code',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='工号'),
        ),
    ]