# Generated by Django 2.0.4 on 2019-04-21 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_auto_20190418_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='default_tax',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.BaseTax', verbose_name='默认税'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='code',
            field=models.CharField(default='', max_length=255, verbose_name='唯一编码'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='partner_level',
            field=models.CharField(choices=[('A', 'SVIP'), ('B', 'VIP'), ('C', '高级'), ('D', '中等'), ('E', '普通')], default='E', max_length=255, verbose_name='客户等级'),
        ),
    ]
