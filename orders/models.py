from django.db import models
from shop.models import Product

class Order(models.Model):
    product = models.ForeignKey(Product , on_delete = models.CASCADE)
    size = models.CharField(max_length=15)
    quantity = models.IntegerField()

    def __str__(self):
        return self.product
