# Generated by Django 2.0.4 on 2019-04-21 23:13

import base.utils
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='登录邮箱')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-create_time'],
                'db_table': 'base_user',
            },
        ),
        migrations.CreateModel(
            name='BaseCity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='城市')),
                ('area_code', models.CharField(max_length=255, verbose_name='城市区号')),
                ('car_number', models.CharField(max_length=255, verbose_name='车牌号首字母')),
                ('is_provincial_capital', models.BooleanField(default=False, verbose_name='省会城市')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['-province', '-name'],
                'db_table': 'base_city',
            },
        ),
        migrations.CreateModel(
            name='BaseCountry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='国家')),
                ('short_name', models.CharField(max_length=255, verbose_name='简称(英文)')),
                ('area_code', models.CharField(max_length=255, verbose_name='国家区号')),
                ('national_flag', models.ImageField(default='default_logo.png', storage=base.utils.CustomFileStorage(), upload_to='country_image/', verbose_name='国旗图标')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['name'],
                'db_table': 'base_country',
            },
        ),
        migrations.CreateModel(
            name='BaseProvince',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='省')),
                ('short_name', models.CharField(max_length=255, verbose_name='简称')),
                ('is_active', models.BooleanField(default=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.BaseCountry', verbose_name='所在国家')),
            ],
            options={
                'ordering': ['-name'],
                'db_table': 'base_province',
            },
        ),
        migrations.CreateModel(
            name='BaseSequence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='名称')),
                ('code', models.CharField(max_length=255, unique=True, verbose_name='命名代号(适用模型)')),
                ('prefix', models.CharField(max_length=255, verbose_name='前缀')),
                ('suffix', models.CharField(default='', max_length=255, verbose_name='后缀')),
                ('padding', models.PositiveIntegerField(default=4, verbose_name='填充长度')),
                ('increment', models.PositiveIntegerField(default=1, verbose_name='步长')),
                ('next_number', models.PositiveIntegerField(default=1, verbose_name='下一个号码')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['-name'],
                'db_table': 'base_sequence',
            },
        ),
        migrations.CreateModel(
            name='BaseTax',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='税')),
                ('code', models.CharField(max_length=255, verbose_name='唯一编码')),
                ('tax_type', models.CharField(choices=[('PERSONAL_INCOME_TAX', '个人所得税'), ('INCREMENT_TAX', '增值税'), ('OTHER', '其他')], default='INCREMENT_TAX', max_length=255, verbose_name='税类型')),
                ('compute_type', models.CharField(choices=[('GROUP', '税组'), ('FIXED', '固定'), ('PERCENT', '百分比')], default='PERCENT', max_length=255, verbose_name='计算方法')),
                ('rounding', models.CharField(default='0.00', max_length=255, verbose_name='精度')),
                ('factor', models.CharField(default='13', max_length=255, verbose_name='百分比')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['-name'],
                'db_table': 'base_tax',
            },
        ),
        migrations.CreateModel(
            name='BaseUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='单位')),
                ('code', models.CharField(max_length=255, verbose_name='唯一编码')),
                ('unit_type', models.CharField(choices=[('UNIT', '数量单位'), ('WEIGHT', '质量'), ('TIME', '时间'), ('LENGTH', '长度'), ('OTHER', '其他')], default='UNIT', max_length=255, verbose_name='单位类别')),
                ('factor', models.CharField(default='1', max_length=255, verbose_name='比例')),
                ('rounding', models.CharField(default='0.00', max_length=255, verbose_name='精度')),
                ('compute_type', models.CharField(choices=[('STD', '标准'), ('RIDE', '大于'), ('DIVIDE', '小于')], default='STD', max_length=255, verbose_name='计算方式')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['-unit_type', '-name'],
                'db_table': 'base_unit',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='公司名称')),
                ('code', models.CharField(max_length=255, verbose_name='唯一编码')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
                ('is_active', models.BooleanField(default=True)),
                ('child_dummy_balance', models.CharField(default='0', max_length=255, verbose_name='返点资金余额')),
                ('child_cash_balance', models.CharField(default='0', max_length=255, verbose_name='实际资金余额')),
                ('dummy_discount', models.CharField(default='40', max_length=255, verbose_name='默认返点比例(%)')),
            ],
            options={
                'ordering': ['-name'],
                'db_table': 'base_company',
            },
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='货币')),
                ('code', models.CharField(max_length=255, verbose_name='唯一编码')),
                ('symbol', models.CharField(max_length=255, verbose_name='符号')),
                ('rounding', models.CharField(default='0.00', max_length=255, verbose_name='精度')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['-name'],
                'db_table': 'base_currency',
            },
        ),
        migrations.CreateModel(
            name='CurrencyRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.CharField(default='100', max_length=255, verbose_name='比率')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
                ('is_active', models.BooleanField(default=True)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='currency_rate_list', to='base.Currency', verbose_name='所属货币')),
            ],
            options={
                'ordering': ['create_time'],
                'db_table': 'base_currency_rate',
                'get_latest_by': 'create_time',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='部门名称')),
                ('code', models.CharField(max_length=255, verbose_name='唯一编码')),
                ('desc', models.CharField(default='', max_length=255, verbose_name='详细描述')),
                ('logo', models.ImageField(default='default_logo.png', storage=base.utils.CustomFileStorage(), upload_to='department_logo/', verbose_name='部门Logo')),
                ('is_active', models.BooleanField(default=True)),
                ('department_type', models.CharField(choices=[('NORMAL', '常规'), ('SPECIAL', '特殊'), ('STORE', '子公司门店'), ('OTHER', '其他')], default='NORMAL', max_length=255, verbose_name='部门类型')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Company', verbose_name='所在公司')),
                ('parent_department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child_department_list', to='base.Department', verbose_name='上级部门')),
            ],
            options={
                'ordering': ['-name'],
                'db_table': 'base_department',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_department_manager', models.BooleanField(default=False, verbose_name='部门经理')),
                ('name', models.CharField(max_length=255, verbose_name='员工名称')),
                ('code', models.CharField(max_length=255, verbose_name='工号')),
                ('induction_date', models.DateField(default=datetime.datetime.now, verbose_name='入职日期')),
                ('work_address', models.CharField(default='', max_length=255, verbose_name='工作地址')),
                ('work_email', models.CharField(default='', max_length=255, verbose_name='工作邮箱')),
                ('work_contact', models.CharField(default='', max_length=255, verbose_name='工作联系方式')),
                ('is_active', models.BooleanField(default=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Company', verbose_name='所在公司')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='department_employee_list', to='base.Department', verbose_name='所属部门')),
            ],
            options={
                'ordering': ['-name'],
                'db_table': 'base_employee',
            },
        ),
        migrations.CreateModel(
            name='JobClassification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='职位名称')),
                ('code', models.CharField(max_length=255, verbose_name='唯一编码')),
                ('desc', models.CharField(default='', max_length=255, verbose_name='详细描述')),
                ('requirement', models.CharField(default='', max_length=255, verbose_name='技能要求')),
                ('pub_date', models.DateField(default=datetime.datetime.now, verbose_name='发布日期')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['-name'],
                'db_table': 'base_job',
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='合作伙伴')),
                ('code', models.CharField(default='', max_length=255, verbose_name='唯一编码')),
                ('desc', models.CharField(default='', max_length=255, verbose_name='详细描述')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
                ('is_active', models.BooleanField(default=True)),
                ('partner_level', models.CharField(choices=[('A', 'SVIP'), ('B', 'VIP'), ('C', '高级'), ('D', '中等'), ('E', '普通')], default='E', max_length=255, verbose_name='客户等级')),
                ('is_customer', models.BooleanField(default=False, verbose_name='是否是客户')),
                ('is_supplier', models.BooleanField(default=False, verbose_name='是否是供应商')),
                ('uniform_social_credit_code', models.CharField(default='', max_length=255, verbose_name='企业统一社会信用代码(税号)')),
                ('legal_person', models.CharField(default='', max_length=255, verbose_name='公司法人')),
                ('register_date', models.DateField(default=datetime.datetime.now, verbose_name='成立时间')),
                ('logo', models.ImageField(default='default_logo.png', storage=base.utils.CustomFileStorage(), upload_to='company_logo/', verbose_name='公司Logo')),
                ('web_site', models.URLField(default='', max_length=255, verbose_name='合作伙伴网址')),
                ('contact_info', models.CharField(default='', max_length=255, verbose_name='联系方式')),
                ('email', models.EmailField(default='', max_length=255, verbose_name='合作伙伴邮箱')),
                ('address', models.CharField(default='', max_length=255, verbose_name='详细地址')),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.BaseCity', verbose_name='城市')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company_partner', to='base.Company', verbose_name='所在公司')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.BaseCountry', verbose_name='所在国家')),
                ('default_tax', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.BaseTax', verbose_name='默认税')),
                ('province', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.BaseProvince', verbose_name='省份')),
            ],
            options={
                'ordering': ['-name'],
                'db_table': 'base_partner',
            },
        ),
        migrations.CreateModel(
            name='PartnerTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='名称')),
                ('color', models.CharField(choices=[('red', '红色'), ('blue', '蓝色'), ('green', '绿色'), ('yellow', '黄色')], default='green', max_length=255, verbose_name='颜色')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
                ('is_active', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_partner_tags', to=settings.AUTH_USER_MODEL, verbose_name='所属用户')),
            ],
            options={
                'ordering': ['-name'],
                'db_table': 'base_partner_tag',
            },
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='用户组名')),
                ('code', models.CharField(max_length=255, verbose_name='唯一编码')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
                ('is_active', models.BooleanField(default=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child_group_list', to='base.UserGroup', verbose_name='上级用户组')),
                ('users', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-name'],
                'db_table': 'base_user_group',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(default='default_logo.png', storage=base.utils.CustomFileStorage(), upload_to='user_avatar/', verbose_name='头像')),
                ('real_name', models.CharField(default='', max_length=255, verbose_name='姓名')),
                ('nickname', models.CharField(default='', max_length=255, verbose_name='昵称')),
                ('person_phone', models.CharField(default='', max_length=255, verbose_name='个人联系号码')),
                ('sex', models.CharField(choices=[('MALE', '男'), ('FEMALE', '女'), ('NULL', '未知')], default='NULL', max_length=255, verbose_name='性别')),
                ('id_number', models.CharField(default='', max_length=255, verbose_name='身份证')),
                ('marital_status', models.CharField(choices=[('NO', '未婚'), ('YES', '已婚')], default='NO', max_length=255, verbose_name='婚姻状态')),
                ('home_address', models.CharField(default='', max_length=255, verbose_name='家庭住址')),
                ('birth_day', models.DateField(default=datetime.datetime.now, verbose_name='生日')),
                ('graduate_school', models.CharField(default='', max_length=255, verbose_name='毕业院校')),
                ('is_active', models.BooleanField(default=True)),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.BaseCountry', verbose_name='国籍')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='uid')),
            ],
            options={
                'ordering': ['-real_name'],
                'db_table': 'base_user_info',
            },
        ),
        migrations.AddField(
            model_name='partner',
            name='tags',
            field=models.ManyToManyField(blank=True, to='base.PartnerTag', verbose_name='标签'),
        ),
        migrations.AddField(
            model_name='employee',
            name='job',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.JobClassification', verbose_name='职位'),
        ),
        migrations.AddField(
            model_name='employee',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='uid'),
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
        migrations.AddField(
            model_name='company',
            name='parent_company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child_company_list', to='base.Company', verbose_name='上级公司'),
        ),
        migrations.AddField(
            model_name='basesequence',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Company', verbose_name='所属公司'),
        ),
        migrations.AddField(
            model_name='basecity',
            name='province',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.BaseProvince', verbose_name='所在省份'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.Company', verbose_name='所在公司'),
        ),
    ]
