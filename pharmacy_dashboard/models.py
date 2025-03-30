from django.db import models
from django.contrib.auth.models import User  # Import Django's User model


class Category(models.Model):
    category = models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return self.category
    

class Product(models.Model):
    pharmacy = models.ForeignKey(User, on_delete=models.CASCADE)  
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=250, default="", null=True, blank=True)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    available_quantity = models.IntegerField(default=0)
    product_image = models.ImageField(upload_to='product_images')
    is_prescription_needed = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.product_id} - {self.product_name} - {self.pharmacy.username}"

