# Generated by Django 2.2.4 on 2019-09-29 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0022_auto_20190928_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='coupon',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='coupon.Coupon'),
        ),
    ]
