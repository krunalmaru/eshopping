from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Category,Subcategory, Product
# Create your views here.
def home(request):
    category = Category.objects.all()
    categoryid = request.GET.get('category')
    if categoryid:
        product = Product.objects.filter(subcategory=categoryid).order_by('-id')
    else:
        product = Product.objects.all()
        
    context = {'category':category, 'product':product}
    return  render(request,'app/home.html',context)

def myaccount(request):
    return render(request, 'accounts/registration.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username Already Exist')
            return redirect('login')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email Already Exist')
            return redirect('login')
        user = User(username=username,email=email)
        user.set_password(password)
        user.save()
        return redirect('login')



def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid Username and Password')
            return redirect('login')