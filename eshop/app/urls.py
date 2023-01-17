from django.urls import path,include
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('account/myaccount/', views.myaccount, name="myaccount"),
    path('account/registration/', views.register, name='userregister'),
    path('account/userlogin/', views.userlogin, name='userlogin'),



] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
