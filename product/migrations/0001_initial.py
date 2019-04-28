# Generated by Django 2.0.4 on 2019-04-28 17:01

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import product.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_usage_type', models.CharField(choices=[('service', '服务类'), ('virtual', '虚拟类'), ('stock', '库存类')], default='stock', max_length=255, verbose_name='产品使用方式分类')),
                ('can_sale', models.BooleanField(default=True, verbose_name='能销售')),
                ('can_purchase', models.BooleanField(default=True, verbose_name='能采购')),
                ('product_sale_type', models.CharField(choices=[('pre_sale', '预售'), ('normal', '正常销售'), ('stop', '停售'), ('sold_out', '下架')], default='normal', max_length=255, verbose_name='销售属性')),
                ('name', models.CharField(max_length=255, verbose_name='产品名称')),
                ('code', models.CharField(default='', max_length=255, verbose_name='代号')),
                ('description', models.CharField(default='', max_length=255, verbose_name='产品详细描述')),
                ('barcode', models.CharField(default='', max_length=255, verbose_name='商品条码')),
                ('product_rank', models.IntegerField(default=1, verbose_name='产品热度')),
                ('product_image', models.CharField(default='default_logo.png', max_length=255, verbose_name='产品图片路径')),
                ('product_length', models.CharField(max_length=255, verbose_name='长')),
                ('product_width', models.CharField(max_length=255, verbose_name='宽')),
                ('product_height', models.CharField(max_length=255, verbose_name='高')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='Create Time')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ProductBrand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='品牌')),
                ('code', models.CharField(default='', max_length=255, verbose_name='代号')),
                ('rank', models.IntegerField(default=1, verbose_name='热度')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='Create Time')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='产品类别')),
                ('code', models.CharField(default='', max_length=255, verbose_name='代号')),
                ('rank', models.IntegerField(default=1, verbose_name='热度')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='Create Time')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ProductPriceList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=product.models._get_default_name, max_length=255, verbose_name='产品价格单')),
                ('original_price', models.CharField(default='1', max_length=255, verbose_name='成本价')),
                ('purchase_price', models.CharField(default='1', max_length=255, verbose_name='采购价')),
                ('sale_price', models.CharField(default='1', max_length=255, verbose_name='销售价')),
                ('start_date', models.DateField(default=datetime.datetime.now, verbose_name='开始时间')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='结束时间')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='Create Time')),
                ('done_time', models.DateTimeField(blank=True, null=True, verbose_name='审核完成时间')),
                ('state', models.CharField(choices=[('cancel', '取消'), ('draft', '草稿'), ('submitted', '提交审核后'), ('in_review', '审核中'), ('completed', '审核完成'), ('done', '单据完成'), ('locked', '锁定')], default='draft', max_length=255, verbose_name='单据状态')),
                ('is_active', models.BooleanField(default=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='base.Company', verbose_name='所属公司')),
                ('create_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='创建用户')),
                ('price_uom', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='base.BaseUnit', verbose_name='价格单位')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product_price_list', to='product.Product', verbose_name='所属产品')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ProductTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='产品标签')),
                ('rank', models.IntegerField(default=1, verbose_name='热度')),
                ('color', models.CharField(choices=[('red', '红'), ('blue', '蓝'), ('green', '绿'), ('yellow', '黄'), ('white', '白')], default='white', max_length=255, verbose_name='标签颜色')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='Create Time')),
                ('is_active', models.BooleanField(default=True)),
                ('create_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_tags', to=settings.AUTH_USER_MODEL, verbose_name='产品标签')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='brand_products', to='product.ProductBrand', verbose_name='产品品牌'),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='category_products', to='product.ProductCategory', verbose_name='产品标签'),
        ),
        migrations.AddField(
            model_name='product',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='company_products', to='base.Company', verbose_name='所属公司'),
        ),
        migrations.AddField(
            model_name='product',
            name='default_unit_uom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product_default_unit_uom', to='base.BaseUnit', verbose_name='产品默认数量单位'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_volume_uom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product_volume_uom', to='base.BaseUnit', verbose_name='产品体积单位'),
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(blank=True, to='product.ProductTag'),
        ),
    ]