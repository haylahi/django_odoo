# Generated by Django 2.0.4 on 2019-04-28 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_auto_20190428_1823'),
    ]

    operations = [
        migrations.AddField(
            model_name='examination',
            name='is_create_record',
            field=models.BooleanField(default=False, verbose_name='创建了考试记录'),
        ),
    ]
