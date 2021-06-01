from django.http import HttpResponse
from django.shortcuts import render, redirect
from products.models.product import Product
from products.models.category import Category
from django.views import View


# from django.contrib.auth.hashers import make_password, check_password
# from django.shortcuts import render, redirect
# from .models.product import Product
# from .models.category import Category
# from .models.customer import Customer
# from django.views import View

# pehle views.p tha products  me

# print(make_password('1234'))
# print(check_password( '1234','pbkdf2_sha256$216000$sEtA1cErPJ2s$kAlbicjqif911iouwGgFDnaGS1NjVrXCMGUWwT1t7XQ='))

class Index(View):

    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity == 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        # print(cart)
        request.session['cart'] = cart
        # print(request.session['cart'])
        return redirect('homepage')

    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        products = None
        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')
        if categoryID:
            products = Product.get_all_products_by_categoryid(categoryID)
        else:
            products = Product.get_all_products();
        data = {}
        data['products'] = products
        data['categories'] = categories
        print("hi", request.session.get('f'), request.session.get('email'))
        # print(request.session.get('customer_id'))
        return render(request, 'index.html', data)


''''
def index(request):
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_all_products_by_categoryid(categoryID)
    else:
        products = Product.get_all_products();
    data = {}
    data['products'] = products
    data['categories'] = categories
    print("hi",request.session.get('f'),request.session.get('email'))
    #print(request.session.get('customer_id'))
    return render(request, 'index.html', data)
'''


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


'''
def validateCustomer(customer):
    error_message = None;

    if customer.isExists():
        error_message = 'Email Address Already Registered..'

    return error_message'''

'''
def registerUser(request):
    postData = request.POST
    first_name = postData.get('firstname')
    last_name = postData.get('lastname')
    phone = postData.get('phone')
    email = postData.get('email')
    password = postData.get('password')
    # validation
    value = {
        'first_name': first_name,
        'last_name': last_name,
        'phone': phone,
        'email': email
    }

    error_message = None
    customer = Customer(first_name=first_name,
                        last_name=last_name,
                        phone=phone,
                        email=email,
                        password=password)
    error_message = validateCustomer(customer)

    if not error_message:
        print(first_name, last_name, phone, email, password)
        customer.password = make_password(customer.password)
        # customer.save()
        customer.register()
        return redirect('homepage')

    else:
        data = {
            'error': error_message,
            'values': value
        }

    return render(request, 'signup.html', data)'''

'''
class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }

        error_message = None
        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)
        error_message = self.validateCustomer(customer)

        if not error_message:
            print(first_name, last_name, phone, email, password)
            customer.password = make_password(customer.password)
            # customer.save()
            customer.register()
            return redirect('homepage')

        else:
            data = {
                'error': error_message,
                'values': value
            }

        return render(request, 'signup.html', data)

    def validateCustomer(self, customer):
        error_message = None;

        if customer.isExists():
            error_message = 'Email Address Already Registered..'

        return error_message'''

'''
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        return registerUser(request)'''

'''
class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        pasword = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(pasword, customer.password)
            if flag:
                return redirect('homepage')
            else:
                error_message = 'Email or Password invalid !!!'
        else:
            error_message = 'Email or Password invalid !!!'
        # print(customer)
        # print(email)
        return render(request, 'login.html', {'error': error_message})'''

'''
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        email = request.POST.get('email')
        pasword = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(pasword, customer.password)
            if flag:
                return redirect('homepage')
            else:
                error_message = 'Email or Password invalid !!!'
        else:
            error_message = 'Email or Password invalid !!!'
        # print(customer)
        # print(email)
        return render(request, 'login.html', {'error': error_message})'''
