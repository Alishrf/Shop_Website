# Generated by Django 2.2.4 on 2019-08-27 14:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20190827_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='release_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 27, 19, 20, 37, 665953)),
        ),
    ]