# Generated by Django 2.2.4 on 2019-10-07 13:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtor', '0046_auto_20191007_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='hire_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 7, 16, 43, 31, 925884)),
        ),
    ]