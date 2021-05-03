from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new', views.new),
    path('cart', views.cart),
    path('getcookie', views.getcookie),
    path('setcookie', views.setcookie)

]