# Generated by Django 2.2.4 on 2019-09-17 10:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupon', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='code',
            field=models.CharField(default=0, max_length=25),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='expiration_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2019, 9, 17, 14, 44, 25, 553211)),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='off',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=100),
        ),
    ]
