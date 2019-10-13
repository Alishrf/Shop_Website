from django.db import models
from datetime import datetime

class Realtor(models.Model):
    name = models.CharField(max_length = 30 )
    post = models.CharField(max_length = 30)
    description = models.TextField(blank=True)
    email = models.EmailField()
    image = models.ImageField(upload_to = 'photos/realtors/')
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default = datetime.now())

    def __str__(self):
        return self.name

