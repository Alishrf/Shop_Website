# Generated by Django 2.2.4 on 2019-09-18 07:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtor', '0019_auto_20190918_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='hire_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 18, 12, 13, 29, 200152)),
        ),
    ]
