from django.db import models

class Categories(models.Model):
   categori_name = models.CharField(max_length = 10)
         
   def __str__(self):
      return self.categori_name
