from django.db import models
from datetime import datetime


# Create your models here.
class Coupon(models.Model):
    code = models.CharField(max_length= 25, default= 0, unique=True ,blank=True )
    off = models.DecimalField(max_digits= 100 ,decimal_places=1,default= 0,blank=True )
    expiration_date = models.DateTimeField(default = datetime.now , blank = True )

    def __str__(self):
        return str(self.id) + '_ ( off = ' + str(self.off) +' )'    
