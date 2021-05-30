from django.contrib import admin
from django.urls import path
from . import views
from .views import index, signup

urlpatterns = [
    path('', index , name='homepage'),
    path('new', views.new),
    path('cart', views.cart),
    path('getcookie', views.getcookie),
    path('setcookie', views.setcookie),
    path('signup', signup)
]
