# Generated by Django 2.2.4 on 2019-09-20 12:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0026_auto_20190920_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='release_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 20, 17, 28, 59, 713586)),
        ),
    ]
