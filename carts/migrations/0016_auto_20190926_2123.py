# Generated by Django 2.2.4 on 2019-09-26 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0015_auto_20190926_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='coupon',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='coupon.Coupon'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='subtotal',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='total',
            field=models.FloatField(blank=True),
        ),
    ]
