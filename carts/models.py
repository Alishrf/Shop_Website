from django.db import models
from orders.models import Order
from coupon.models import Coupon

class Cart(models.Model):
    orders = models.ManyToManyField(Order,blank = True)
    subtotal = models.FloatField(blank = True)
    total = models.FloatField(blank = True)
    coupon = models.ForeignKey(Coupon,on_delete = models.DO_NOTHING,blank = True)


