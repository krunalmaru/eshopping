from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('accounts/myaccount/', views.myaccount, name="myaccount"),
    path('accounts/registration/', views.register, name='register'),
    path('accounts/login/', views.userlogin, name='userlogin'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
