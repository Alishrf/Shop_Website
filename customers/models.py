from django.db import models
from django.contrib.auth.models import User
from carts.models import Cart

class Customer(models.Model):
    user = models.OneToOneField(User,on_delete = models.DO_NOTHING)
    cart = models.OneToOneField(Cart,blank= True,on_delete = models.DO_NOTHING)
    address = models.CharField(blank=True , max_length=100)
    
    def __str__(self):
        return self.user.username    

