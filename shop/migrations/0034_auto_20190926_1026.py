# Generated by Django 2.2.4 on 2019-09-26 06:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0033_auto_20190925_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='release_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 26, 10, 26, 25, 1774)),
        ),
    ]
