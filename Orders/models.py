from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Orders(models.Model):

    user=models.CharField(max_length=200)
    img=models.CharField(max_length=500)
    product_name = models.CharField(max_length=200)  # Name of the product
    Width = models.IntegerField()  # Width of the product (in some unit, e.g., cm)
    Height = models.IntegerField()  # Height of the product (in some unit, e.g., cm)
    Quantity = models.IntegerField()  # Quantity available
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    total=models.DecimalField(max_digits=10, decimal_places=2)# Price of the product, supports decimals
    Payment_received=models.BooleanField(default=False)
    Type=models.CharField(max_length=500)
    Color=models.CharField(max_length=500)
    Name=models.CharField(max_length=500)
    Phone=models.CharField(max_length=500)
    Street=models.CharField(max_length=500)
    PostalCode=models.CharField(max_length=500)
    City=models.CharField(max_length=500)
    Note=models.CharField(max_length=500)

    def __str__(self):


        return self.user  # Show product_name in the admin



class Order_from_offer(models.Model):

    user_name=models.CharField(max_length=200)
    Telephone=models.CharField(max_length=500)
    Email = models.CharField(max_length=200)  # Name of the product
    Order =models.CharField(max_length=200)   # Width of the product (in some unit, e.g., cm)
    # file = models.IntegerField()  # Height of the product (in some unit, e.g., cm)

    def __str__(self):
        return self.user_name
