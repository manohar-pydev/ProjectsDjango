from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=100)
    price = models.FloatField()
    brand = models.CharField(max_length=100)
    sku = models.CharField(max_length=100)
    thumbnail = models.URLField(max_length=100)