# Generated by Django 2.0.4 on 2019-04-19 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0004_auto_20190419_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockpickingtype',
            name='address',
            field=models.CharField(max_length=255, verbose_name='仓库位置地址'),
        ),
        migrations.AlterField(
            model_name='stockpickingtype',
            name='short_name',
            field=models.CharField(max_length=255, verbose_name='简称'),
        ),
    ]
