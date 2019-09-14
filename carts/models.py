from django.db import models
from orders.models import Order
from coupon.models import coupon

class Cart(models.Model):
    orders = models.ManyToManyField(Order,blank = True)
    subtotal = models.FloatField(default = 0)
    total = models.FloatField(default = 0)
    coupon = models.ForeignKey(coupon,on_delete =models.DO_NOTHING ,default = 0)


