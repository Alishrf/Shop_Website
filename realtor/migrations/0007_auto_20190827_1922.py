# Generated by Django 2.2.4 on 2019-08-27 14:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtor', '0006_auto_20190827_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='hire_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 27, 19, 22, 45, 624123)),
        ),
    ]
