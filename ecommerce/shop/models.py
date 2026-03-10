from django.db import models

class Product(models.Model):
    thumbnail = models.URLField()
    name = models.CharField(max_length=64)
    price = models.FloatField()
