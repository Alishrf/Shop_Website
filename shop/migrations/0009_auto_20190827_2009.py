# Generated by Django 2.2.4 on 2019-08-27 15:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_auto_20190827_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='release_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 27, 20, 9, 45, 569164)),
        ),
    ]
