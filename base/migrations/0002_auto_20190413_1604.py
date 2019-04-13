# Generated by Django 2.0.4 on 2019-04-13 16:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseCity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='城市')),
                ('code', models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='唯一编码')),
                ('area_code', models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='城市区号')),
                ('car_number', models.CharField(blank=True, max_length=255, null=True, verbose_name='车牌号首字母')),
            ],
            options={
                'db_table': 'base_city',
            },
        ),
        migrations.CreateModel(
            name='BaseCountry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='国家')),
                ('code', models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='唯一编码')),
                ('area_code', models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='国家区号')),
                ('national_flag', models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='国旗')),
            ],
            options={
                'db_table': 'base_country',
            },
        ),
        migrations.CreateModel(
            name='BaseDistrict',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='区')),
                ('code', models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='唯一编码')),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.BaseCity', verbose_name='所在城市')),
            ],
            options={
                'db_table': 'base_district',
            },
        ),
        migrations.CreateModel(
            name='BaseProvince',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='省')),
                ('code', models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='唯一编码')),
                ('short_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='简称')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.BaseCountry', verbose_name='所在国家')),
            ],
            options={
                'db_table': 'base_province',
            },
        ),
        migrations.CreateModel(
            name='BaseTax',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='税')),
                ('code', models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='唯一编码')),
            ],
            options={
                'db_table': 'base_tax',
            },
        ),
        migrations.CreateModel(
            name='BaseUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='货币')),
                ('code', models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='唯一编码')),
            ],
            options={
                'db_table': 'base_unit',
            },
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='货币')),
                ('code', models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='唯一编码')),
            ],
            options={
                'db_table': 'base_currency',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='部门名称')),
                ('code', models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='唯一编码')),
            ],
            options={
                'db_table': 'base_department',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='部门名称')),
                ('code', models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='唯一编码')),
            ],
            options={
                'db_table': 'base_employee',
            },
        ),
        migrations.AddField(
            model_name='company',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='company',
            name='legal_person',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='公司法人'),
        ),
        migrations.AddField(
            model_name='employee',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.Company', verbose_name='所在公司'),
        ),
        migrations.AddField(
            model_name='employee',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.Department', verbose_name='所属部门'),
        ),
        migrations.AddField(
            model_name='employee',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='uid'),
        ),
        migrations.AddField(
            model_name='department',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.Company', verbose_name='所在公司'),
        ),
        migrations.AddField(
            model_name='basecity',
            name='province',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.BaseProvince', verbose_name='所在省份'),
        ),
        migrations.AddField(
            model_name='company',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.BaseCountry', verbose_name='所在国家'),
        ),
        migrations.AddField(
            model_name='company',
            name='default_currency',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.Currency', verbose_name='默认货币'),
        ),
        migrations.AddField(
            model_name='company',
            name='default_tax',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.BaseTax', verbose_name='默认税'),
        ),
    ]
