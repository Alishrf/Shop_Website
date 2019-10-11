from django.shortcuts import render
from shop.models import Product
from realtor.models import Realtor
from django.contrib.auth.models import User
from customers.models import Customer


def index(request):
    if request.user.is_authenticated:
        customer = Customer.objects.get( user = request.user )
        context = {
            'cart_size' : len(customer.cart.orders.all())
        }
        return render(request,'pages/index.html',context)
    return render(request,'pages/index.html')
def about(request):
    realtors = Realtor.objects.all()
    context = {
        'realtors' : realtors ,
    }
    if request.user.is_authenticated:
        customer = Customer.objects.get( user = request.user )
        context = {
            'realtors' : realtors ,
            'cart_size' : len(customer.cart.orders.all()),
        }
    return render(request,'pages/about.html',context)   