# Generated by Django 2.2.4 on 2019-09-18 07:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0021_auto_20190918_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='release_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 18, 12, 25, 3, 168212)),
        ),
    ]
