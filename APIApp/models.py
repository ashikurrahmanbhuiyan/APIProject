from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=21)
    price = models.IntegerField()
    description = models.CharField(max_length=100)