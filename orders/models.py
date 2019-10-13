from django.db import models
from shop.models import Product

class Order(models.Model):
    product = models.ForeignKey(Product , on_delete = models.DO_NOTHING)
    size = models.CharField(max_length=15)
    quantity = models.IntegerField()
    total_price = models.FloatField(default = 0 )

    def __str__(self):
        return str(self.product) + '(' + str(self.id) + ')'
