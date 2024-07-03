from django.db import models

# Create your models here.
from django.db import models
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

import datetime


from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Customer(models.Model) :
     first_name = models.CharField(max_length=50)
     last_name = models.CharField(max_length=50)
     phone_number=models.CharField(max_length=30)
     email= models.EmailField(max_length=100)
     password= models.CharField(max_length=45)

     def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Product (models.Model) :
    name = models.CharField(max_length=50)
    description = models.CharField (max_length=250 , default='', blank=True)
    price= models.DecimalField (default=0, decimal_places=2 , max_digits=12)
    category= models.ForeignKey ('shop.Category', on_delete= models.CASCADE)
    pictur= models.ImageField(upload_to="upload/products/")



    def __str__(self):
      return self.name
    
class Order(models.Model) :
       product = models.ForeignKey(Product, on_delete= models.CASCADE)
       Customer= models.ForeignKey(Customer, on_delete= models.CASCADE)
       quantity= models.IntegerField(default=1)
       address= models.CharField (max_length=400, default="",blank=False)
       phone= models.CharField(max_length=20, blank=True)
       date= models.DateField(default=datetime.datetime.today())
       status= models.BooleanField(default=False)
   
       def __str__(self):
        return self.name
 
