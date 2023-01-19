from django.contrib import admin
from .models import Category,Subcategory,Product,Contactus,Order,Brand,Productimage
# Register your models here.

class Product_Images(admin.TabularInline):
    model = Productimage

class ProductAdmin(admin.ModelAdmin):
    inlines = (Product_Images,)

admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Product,ProductAdmin)
admin.site.register(Contactus)
admin.site.register(Order)
admin.site.register(Brand)
admin.site.register(Productimage) 