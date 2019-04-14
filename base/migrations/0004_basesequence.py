# Generated by Django 2.0.4 on 2019-04-14 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_basecity_is_provincial_capital'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseSequence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='名称')),
                ('code', models.CharField(max_length=255, unique=True, verbose_name='命名代号(适用模型)')),
                ('prefix', models.CharField(max_length=255, verbose_name='前缀')),
                ('suffix', models.CharField(blank=True, max_length=255, null=True, verbose_name='后缀')),
                ('padding', models.PositiveIntegerField(default=4, verbose_name='填充长度')),
                ('increment', models.PositiveIntegerField(default=1, verbose_name='步长')),
                ('next_number', models.PositiveIntegerField(default=1, verbose_name='下一个号码')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'base_sequence',
            },
        ),
    ]
