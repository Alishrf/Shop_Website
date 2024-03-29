# Generated by Django 2.2.4 on 2019-08-27 15:00

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('shop', '0007_auto_20190827_1922'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='categories',
        ),
        migrations.AddField(
            model_name='product',
            name='categorie',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='categories.Categories'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='release_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 27, 19, 29, 50, 383685)),
        ),
    ]
