from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=70, blank=False)
    description = models.CharField(max_length=200, blank=True)
    price = models.FloatField(blank=False)
    active = models.BooleanField(default=True)
