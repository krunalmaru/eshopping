from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Category,Subcategory, Product,Contactus,Order
from cart.cart import Cart
from django.contrib.auth.decorators import login_required
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

@login_required(login_url='/accounts/login')
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect('home')

@login_required(login_url='/accounts/login')
def item_clear(request,id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")

@login_required(login_url='/accounts/login')
def item_increment(request,id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")

@login_required(login_url='/accounts/login')
def item_decrement(request,id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")

@login_required(login_url='/accounts/login')
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")

@login_required(login_url='/accounts/login')
def cart_detail(request):
    return render(request,'cart_detail.html')

def contact(request):
    if request.method == 'POST':
        contact = Contactus(
        name = request.POST.get('name'),
        email = request.POST.get('email'),
        subject = request.POST.get('subject'),
        )
        contact.save()
        return redirect('contactus')

    return render(request, 'contact.html')

def checkout(request):
    if request.method == 'POST':
        phone= request.POST.get('phone')
        address = request.POST.get('address')
        pincode = request.POST.get('pincode')
        cart = request.session.get('cart')
        uid = request.session.get('_auth_user_id')
        user = User.objects.get(pk=uid)
        print(phone,address,pincode,cart,user)
        for i in cart:
            print(i)
            a = (int(cart[i]['price']))
            b = cart[i]['quantity']
            total = a * b
            order = Order(
                user = user,
                product = cart[i]['name'],
                quantity = cart[i]['quantity'],
                price = cart[i]['price'],
                image = cart[i]['image'],
                address = address,
                pincode=pincode,
                phone=phone,
                total = total
            )
            order.save()
        request.session['cart'] = {}
        return redirect('home')
    return HttpResponse("this is checkout")

def yourorder(request):
    uid = request.session.get('_auth_user_id')
    user = User.objects.get(pk=uid)
    order = Order.objects.filter(user=user)
    context = {'order':order}
    return render(request, 'yourorder.html',context)