# Generated by Django 2.2.4 on 2019-09-18 07:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_auto_20190918_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='release_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 18, 12, 3, 2, 58147)),
        ),
    ]
