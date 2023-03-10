from django.urls import path,include
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('account/myaccount/', views.myaccount, name="myaccount"),
    path('account/registration/', views.register, name='userregister'),
    path('account/userlogin/', views.userlogin, name='userlogin'),
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
    path('contact/', views.contact, name='contactus'),
    path('checkout/', views.checkout, name='checkout'),
    path('yourorder/', views.yourorder, name='yourorder'),
    path('allproduct/', views.allproduct, name='allproduct'),
    path('allproduct/<int:id>/', views.productdetail, name="productdetail"),
    path('search/', views.search, name='searchproduct'),



] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
