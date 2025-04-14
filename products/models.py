

from django.db import models
from django.utils.timezone import datetime


# Create your models here.
class products(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    is_available = models.BooleanField(default= False)
    created_at = models.DateTimeField(default= datetime.now)
