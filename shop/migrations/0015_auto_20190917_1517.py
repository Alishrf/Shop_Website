# Generated by Django 2.2.4 on 2019-09-17 10:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_auto_20190917_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='release_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 17, 15, 17, 29, 728698)),
        ),
    ]