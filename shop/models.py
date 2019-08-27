from django.db import models
from datetime import datetime
from realtor.models import Realtor

class Product(models.Model):
    realtor = models.ForeignKey(Realtor,on_delete=models.CASCADE)
    title = models.CharField(max_length = 30)
    quantity_small = models.IntegerField(default=0)
    quantity_medium = models.IntegerField(default=0)
    quantity_large = models.IntegerField(default=0)
    quantity_extralarge = models.IntegerField(default=0)  
    price = models.FloatField(default =0)
    description = models.TextField(blank=True)
    is_public = models.BooleanField(default=True)
    release_time = models.DateTimeField(default = datetime.now())
    main_image = models.ImageField(upload_to = 'photos/%Y/%m/%d')

    def __str__(self):
        return self.title



