from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
    
class products(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    color = models.CharField(max_length=25)
    image = models.ImageField(upload_to='product-img/')
    stock = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    
    def is_in_stock(self):
        """Returns True if the product is in stock."""
        return self.stock

class Contact(models.Model):
    phone_number = models.CharField(max_length=15)        
    email = models.EmailField(max_length=254,null=True, blank=True)       
    address = models.TextField(null=True, blank=True)         

    def __str__(self):
        return f"{self.phone_number}, {self.email}"
    
class Order(models.Model):
    product = models.ForeignKey(products, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=254,null=True, blank=True) 
    home_district = models.CharField(max_length=100)
    pincode = models.CharField(max_length=6)
    address = models.TextField()
    date_ordered = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default="Pending")

    def __str__(self):
        return f"Order for {self.product.name} by {self.name}"
