# Generated by Django 2.2.4 on 2019-10-06 20:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20190929_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submittedorder',
            name='order_date',
            field=models.DateField(default=datetime.date(2019, 10, 7)),
        ),
        migrations.AlterField(
            model_name='submittedorder',
            name='post_date',
            field=models.DateField(default=datetime.date(2019, 10, 7)),
        ),
    ]
