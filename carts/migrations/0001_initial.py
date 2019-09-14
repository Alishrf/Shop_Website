# Generated by Django 2.2.4 on 2019-09-14 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orders', '0001_initial'),
        ('coupon', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtotal', models.FloatField(default=0)),
                ('total', models.FloatField(default=0)),
                ('coupon', models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='coupon.coupon')),
                ('orders', models.ManyToManyField(blank=True, to='orders.Order')),
            ],
        ),
    ]