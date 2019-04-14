# Generated by Django 2.0.4 on 2019-04-13 22:16

import base.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_auto_20190413_2021'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(storage=base.utils.CustomFileStorage(), upload_to='test/', verbose_name='file')),
            ],
        ),
        migrations.AlterField(
            model_name='basecountry',
            name='national_flag',
            field=models.ImageField(default='country_image/national_flag.png', storage=base.utils.CustomFileStorage(), upload_to='country_image/', verbose_name='国旗图标'),
        ),
    ]