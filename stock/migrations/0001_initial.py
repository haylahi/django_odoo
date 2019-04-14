# Generated by Django 2.0.4 on 2019-04-14 19:10

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='仓库名称')),
                ('code', models.CharField(max_length=255, unique=True, verbose_name='唯一编码')),
                ('location_type', models.CharField(choices=[('VIEW', '视图位置'), ('INTERNAL', '内部位置'), ('SUPPLIER', '供应商位置'), ('CUSTOMER', '客户位置'), ('PRODUCTION', '生产位置')], default='INTERNAL', max_length=255, verbose_name='位置类型')),
                ('is_return_location', models.BooleanField(default=False, verbose_name='是否为退货位置')),
                ('pos_x', models.CharField(blank=True, max_length=255, null=True, verbose_name='X')),
                ('pos_y', models.CharField(blank=True, max_length=255, null=True, verbose_name='Y')),
                ('pos_z', models.CharField(blank=True, max_length=255, null=True, verbose_name='Z')),
                ('is_active', models.BooleanField(default=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='childs', to='stock.StockLocation', verbose_name='上级位置')),
            ],
            options={
                'db_table': 'stock_location',
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='StockWarehouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='仓库名称')),
                ('code', models.CharField(max_length=255, unique=True, verbose_name='唯一编码')),
                ('short_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='简称')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='仓库地址')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
                ('is_active', models.BooleanField(default=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.Company', verbose_name='所在公司')),
            ],
            options={
                'db_table': 'stock_warehouse',
                'ordering': ['-name'],
            },
        ),
        migrations.AddField(
            model_name='stocklocation',
            name='warehouse',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stock.StockWarehouse', verbose_name='所属仓库'),
        ),
    ]
