# Generated by Django 2.0.4 on 2019-04-14 15:24

import base.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_auto_20190414_1507'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='basetax',
            options={'ordering': ['-name']},
        ),
        migrations.AlterField(
            model_name='basecountry',
            name='national_flag',
            field=models.ImageField(blank=True, default='country_image/national_flag.png', null=True, storage=base.utils.CustomFileStorage(), upload_to='country_image/', verbose_name='国旗图标'),
        ),
        migrations.AlterField(
            model_name='department',
            name='logo',
            field=models.ImageField(blank=True, null=True, storage=base.utils.CustomFileStorage(), upload_to='department_logo/', verbose_name='部门Logo'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='logo',
            field=models.ImageField(blank=True, null=True, storage=base.utils.CustomFileStorage(), upload_to='company_logo/', verbose_name='公司Logo'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='avatar',
            field=models.ImageField(blank=True, null=True, storage=base.utils.CustomFileStorage(), upload_to='user_avatar/', verbose_name='头像'),
        ),
    ]
