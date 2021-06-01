from django.urls import path
from products.views import signup, login, home
from products.views.home import Index

# from django.contrib import admin
# from . import views
# from .views import home
# from .views import index, Signup, Login

urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    # path('new', views.new), ye views.py me tha but abhi home.py me he jab chahiye tab home.new karna
    # path('cart', views.cart),
    # path('getcookie', views.getcookie),
    # path('setcookie', views.setcookie),
    path('signup', signup.Signup.as_view(), name='signup'),
    path('login', login.Login.as_view(), name='login')

]
