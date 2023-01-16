from django.shortcuts import render
from .models import Category,Subcategory
# Create your views here.
def home(request):
    category = Category.objects.all()
    context = {'category':category}
    return  render(request,'app/home.html',context)
