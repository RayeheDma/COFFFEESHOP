from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

import datetime
class Category(models.Model) :
    name = models.CharField(max_length=50)

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
    category= models.ForeignKey(Category, on_delete= models.CASCADE , default=1)
    pictur= models.ImageField(upload_to="upload/products/")
    star = models.IntegerField(default=0, validators=[MaxValueValidator(5),MinValueValidator(0)])
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0 ,decimal_places=0 , max_digits=12)


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
        return self.product