# Generated by Django 2.2.4 on 2019-09-21 09:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtor', '0029_auto_20190921_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='hire_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 21, 13, 40, 50, 237141)),
        ),
    ]
