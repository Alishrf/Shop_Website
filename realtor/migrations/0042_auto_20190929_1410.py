# Generated by Django 2.2.4 on 2019-09-29 10:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtor', '0041_auto_20190928_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='hire_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 29, 14, 10, 27, 130589)),
        ),
    ]
