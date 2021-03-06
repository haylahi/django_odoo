# Generated by Django 2.0.4 on 2019-05-01 16:46

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0009_auto_20190429_0308'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='名称')),
                ('create_time', models.DateTimeField(default=datetime.datetime.now)),
                ('is_active', models.BooleanField(default=True)),
                ('create_teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='school.Teacher')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='examination',
            name='test_tags',
            field=models.ManyToManyField(blank=True, to='school.TestTag', verbose_name='标签'),
        ),
    ]
