# Generated by Django 2.0.4 on 2019-04-26 19:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20190424_2346'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=255, verbose_name='所属APP')),
                ('model_name', models.CharField(max_length=255, verbose_name='所属模型')),
                ('model_id', models.CharField(max_length=255, verbose_name='所属对象ID')),
                ('file_name', models.CharField(max_length=255, verbose_name='原始文件名')),
                ('file_suffix', models.CharField(default='.txt', help_text='保存形式为 xxx.txt', max_length=255, verbose_name='文件后缀名')),
                ('file_path', models.CharField(max_length=255, unique=True, verbose_name='文件相对路径')),
                ('file_coding', models.CharField(default='utf8', max_length=255, verbose_name='文件编码格式')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['-create_time'],
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='合作伙伴名称')),
                ('code', models.CharField(default='', max_length=255, verbose_name='Code')),
                ('description', models.CharField(default='', max_length=255, verbose_name='描述')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='useroperationlog',
            name='result',
            field=models.CharField(default='', max_length=255, verbose_name='操作结果'),
        ),
    ]
