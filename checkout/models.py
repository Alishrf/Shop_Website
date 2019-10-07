from django.db import models
from datetime import date
from carts.models import Cart

class SubmittedOrder(models.Model):
    cart = models.ForeignKey(Cart , on_delete = models.DO_NOTHING)
    country = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    company_name = models.CharField(max_length=20 , blank=True)
    address = models.TextField(max_length=60)
    state = models.CharField(max_length=20)
    posta = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    order_notes = models.TextField(max_length=200)
    is_Posted = models.BooleanField(default=False)
    order_date = models.DateField(default = date.today())
    post_date = models.DateField(default = date.today())

    def __str__(self):
        return self.first_name + ' ' + self.last_name