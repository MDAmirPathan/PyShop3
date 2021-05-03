from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def cart(request):
    products = Product.objects.all()
    return render(request, 'tp.html', {'products': products})

def new(request):
    return HttpResponse('New Products')


def setcookie(request):
    response = HttpResponse("Cookie Set")
    response.set_cookie('java-tutorial', 'javatpoint.com')
    return response


def getcookie(request):
    tutorial = request.COOKIES['java-tutorial']
    return HttpResponse("java tutorials @: " + tutorial)
