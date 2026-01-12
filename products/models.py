from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=200)  # Name of the product
    Width = models.IntegerField()  # Width of the product (in some unit, e.g., cm)
    Height = models.IntegerField()  # Height of the product (in some unit, e.g., cm)
    Quantity = models.IntegerField()  # Quantity available
    Price = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the product, supports decimals

    def __str__(self):
        return self.product_name  # Show product_name in the admin



class Offer(models.Model):
    name=models.CharField(max_length=200 ,default="offer",editable=False)
    offer=models.BooleanField(default=False)