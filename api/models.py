from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255, default="Title")
    description = models.TextField(blank=True)
    brand = models.CharField(max_length=100, default="Unknown")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    thumbnail = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
