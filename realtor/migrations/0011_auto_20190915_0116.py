# Generated by Django 2.2.4 on 2019-09-14 20:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtor', '0010_auto_20190912_0104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='hire_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 15, 1, 16, 19, 515777)),
        ),
    ]