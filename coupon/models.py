from django.db import models


# Create your models here.
class coupon(models.Model):
    code = models.CharField(max_length= 25)
    off = models.DecimalField(max_digits= 100 ,decimal_places=1)
    expiration_date = models.DateField()
    