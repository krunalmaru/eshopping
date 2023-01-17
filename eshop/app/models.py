from django.db import models

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

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=False, default='')
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE,null=False, default='')
    image = models.ImageField(upload_to='product/img')
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    tax = models.IntegerField(null=True)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name