# Generated by Django 2.2.4 on 2019-09-11 20:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtor', '0009_auto_20190827_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='hire_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 12, 1, 4, 57, 327690)),
        ),
    ]
