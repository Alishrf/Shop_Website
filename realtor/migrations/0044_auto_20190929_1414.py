# Generated by Django 2.2.4 on 2019-09-29 10:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtor', '0043_auto_20190929_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='hire_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 29, 14, 14, 38, 734572)),
        ),
    ]
