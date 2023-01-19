from django.db import models
from django.contrib.auth.models import User
import datetime
from ckeditor.fields import RichTextField
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.name

class Subcategory(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    Availability = (('In Stock','In stock'),
        ('Out Of stock', 'Out Of Stock')
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=False, default='')
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE,null=False, default='')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='product/img')
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    tax = models.IntegerField(null=True, blank=True)
    description = RichTextField()
    date = models.DateField(auto_now_add=True)
    availability = models.CharField(choices=Availability,max_length=100,null=True)

    def __str__(self) -> str:
        return self.name

class Productimage(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    image_url = models.CharField(max_length=200)

class Contactus(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self) -> str:
        return self.name



class Order(models.Model):
    image = models.ImageField(upload_to='order/image') 
    product = models.CharField(max_length=100, default='')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=5)
    price = models.IntegerField()
    total = models.CharField(max_length=255, default='')
    address = models.TextField()
    phone= models.CharField(max_length=20)
    pincode = models.CharField(max_length=10)
    date = models.DateField(default=datetime.datetime.today)

    def __str__(self) -> str:
        return self.product