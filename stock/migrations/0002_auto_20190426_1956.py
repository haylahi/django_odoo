# Generated by Django 2.0.4 on 2019-04-26 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stocklocation',
            old_name='desc',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='stockwarehouse',
            old_name='desc',
            new_name='description',
        ),
    ]
