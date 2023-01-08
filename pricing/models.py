from django.db import models

# Create your models here.
class BusinessActivity(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return f'Giro del negocio: "{self.name}"'

class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    
    def __str__(self) -> str:
        return f'Categoría: "{self.name}"'
    
class Product(models.Model):
    name = models.CharField(max_length=200)
    categories = models.ManyToManyField(Category, blank=True)
    business_activity = models.ForeignKey(BusinessActivity, on_delete=models.CASCADE)
    image = models.CharField(max_length=300, default="https://picsum.photos/700/500")
    
    def __str__(self) -> str:
        return f'Producto: "{self.name}"'
    
class ProductPrice(models.Model):
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f'Precio del producto "{self.product.name}": ${self.price}'
    
class Pricing(models.Model):
    total = models.DecimalField(max_digits=8, decimal_places=2)
    products = models.ManyToManyField(Product, blank=True)

    