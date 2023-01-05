from django.db import models

# Create your models here.
class Pricing(models.Model):
    total = models.DecimalField(max_digits=8, decimal_places=2)

class Product(models.Model):
    name = models.CharField(max_length=200)

class ProductPricing(models.Model):
    pricing = models.ForeignKey(Pricing, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)