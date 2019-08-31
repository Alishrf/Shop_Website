from django.shortcuts import render
from .models import Product

def shop(request):
    products = Product.objects.order_by('-release_time')
    context = {
        'products' : products
    }
    return render(request,'shop/shop.html' ,context)

