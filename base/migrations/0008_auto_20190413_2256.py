# Generated by Django 2.0.4 on 2019-04-13 22:56

import base.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_auto_20190413_2216'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TestTest',
        ),
        migrations.AlterField(
            model_name='basecountry',
            name='national_flag',
            field=models.ImageField(blank=True, default='country_image/national_flag.png', null=True, storage=base.utils.CustomFileStorage(), unique=True, upload_to='country_image/', verbose_name='国旗图标'),
        ),
    ]