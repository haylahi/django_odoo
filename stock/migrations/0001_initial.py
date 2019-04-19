# Generated by Django 2.0.4 on 2019-04-17 09:53

import datetime
from django.db import migrations, models
import django.db.models.deletion
import stock.models


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
                ('name', models.CharField(max_length=255, verbose_name='仓库名称')),
                ('code', models.CharField(max_length=255, verbose_name='唯一编码')),
                ('location_type', models.CharField(choices=[('VIEW', '视图位置'), ('INTERNAL', '内部位置'), ('SUPPLIER', '供应商位置'), ('CUSTOMER', '客户位置'), ('PRODUCTION', '生产位置')], default='INTERNAL', max_length=255, verbose_name='位置类型')),
                ('is_return_location', models.BooleanField(default=False, verbose_name='是否为退货位置')),
                ('pos_x', models.CharField(default='', max_length=255, verbose_name='X')),
                ('pos_y', models.CharField(default='', max_length=255, verbose_name='Y')),
                ('pos_z', models.CharField(default='', max_length=255, verbose_name='Z')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
                ('is_active', models.BooleanField(default=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='childs', to='stock.StockLocation', verbose_name='上级位置')),
            ],
            options={
                'ordering': ['-name'],
                'db_table': 'stock_location',
            },
        ),
        migrations.CreateModel(
            name='StockMove',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'stock_move',
            },
        ),
        migrations.CreateModel(
            name='StockMoveLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'stock_move_line',
            },
        ),
        migrations.CreateModel(
            name='StockPicking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='调拨单号')),
                ('origin', models.CharField(default='', max_length=255, verbose_name='源单据号')),
                ('note', models.CharField(default='', max_length=255, verbose_name='备注')),
                ('state', models.CharField(choices=[('draft', '草稿'), ('wait', '等待'), ('ready', '就绪'), ('pending', '待审核'), ('done', '完成'), ('cancel', '取消')], default='draft', max_length=255, verbose_name='状态')),
                ('from_contact', models.CharField(default='', max_length=255, verbose_name='源位置联系方式')),
                ('to_contact', models.CharField(default='', max_length=255, verbose_name='目的位置联系方式')),
                ('return_note', models.CharField(default='', max_length=255, verbose_name='退货原因')),
                ('real_price_total', models.CharField(default='', max_length=255, verbose_name='实际含税金额')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
                ('create_date', models.DateField(default=datetime.datetime.today, verbose_name='创建日期')),
                ('expect_date', models.DateField(default=stock.models.datetime.today, verbose_name='预计完成日期')),
                ('done_date', models.DateField(default=stock.models.datetime.today, verbose_name='完成日期')),
                ('is_active', models.BooleanField(default=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Company', verbose_name='所在公司')),
                ('destination_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='destination_locations', to='stock.StockLocation', verbose_name='目的位置')),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Partner', verbose_name='合作伙伴')),
            ],
            options={
                'ordering': ['-create_time', '-name'],
                'db_table': 'stock_picking',
            },
        ),
        migrations.CreateModel(
            name='StockPickingType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='作业类型')),
                ('code', models.CharField(max_length=255, verbose_name='唯一编码')),
                ('short_name', models.CharField(default='', max_length=255, verbose_name='简称')),
                ('address', models.CharField(default='', max_length=255, verbose_name='仓库位置地址')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
                ('is_active', models.BooleanField(default=True)),
                ('diff_type', models.CharField(choices=[('PFU', '总公司从供应商收货'), ('PTC', '总公司对子公司发货'), ('PTU', '总公司对客户发货'), ('PRU', '总公司对供应商退货'), ('CFP', '子公司从总公司收货'), ('CFU', '子公司从供应商收货'), ('CTU', '子公司对客户发货'), ('CRU', '子公司对供应商退货'), ('CRP', '子公司对总公司退货'), ('URP', '客户对总公司退货'), ('URC', '客户对子公司退货')], max_length=255, verbose_name='区分作业类型')),
                ('op_type', models.CharField(choices=[('INBOUND', '供应商'), ('OUTBOUND', '客户'), ('INTERNAL', '内部')], default='INTERNAL', max_length=255, verbose_name='出入站类型')),
                ('show_reserved', models.BooleanField(default=False, verbose_name='显示预留')),
                ('show_lot', models.BooleanField(default=False, verbose_name='显示批次号')),
                ('use_new_lot', models.BooleanField(default=False, verbose_name='是否创建新的批次号')),
                ('use_already_lot', models.BooleanField(default=False, verbose_name='是否使用已有的批次号')),
                ('default_destination_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='default_destination_locations', to='stock.StockLocation', verbose_name='默认目的位置')),
                ('default_source_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='default_source_locations', to='stock.StockLocation', verbose_name='默认来源位置')),
                ('return_picking_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock.StockPickingType', verbose_name='退回的作业类型')),
                ('sequence', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.BaseSequence', verbose_name='序列号')),
            ],
            options={
                'ordering': ['-name'],
                'db_table': 'stock_picking_type',
            },
        ),
        migrations.CreateModel(
            name='StockProductionLot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'stock_production_lot',
            },
        ),
        migrations.CreateModel(
            name='StockQuantity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'stock_quant',
            },
        ),
        migrations.CreateModel(
            name='StockWarehouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='仓库名称')),
                ('code', models.CharField(max_length=255, verbose_name='唯一编码')),
                ('short_name', models.CharField(default='', max_length=255, verbose_name='简称')),
                ('address', models.CharField(max_length=255, verbose_name='仓库地址')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
                ('is_active', models.BooleanField(default=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Company', verbose_name='所在公司')),
            ],
            options={
                'ordering': ['-name'],
                'db_table': 'stock_warehouse',
            },
        ),
        migrations.AddField(
            model_name='stockpickingtype',
            name='warehouse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.StockWarehouse', verbose_name='所属仓库'),
        ),
        migrations.AddField(
            model_name='stockpicking',
            name='picking_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.StockPickingType', verbose_name='作业类型'),
        ),
        migrations.AddField(
            model_name='stockpicking',
            name='source_location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source_locations', to='stock.StockLocation', verbose_name='来源位置'),
        ),
        migrations.AddField(
            model_name='stocklocation',
            name='warehouse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.StockWarehouse', verbose_name='所属仓库'),
        ),
    ]
