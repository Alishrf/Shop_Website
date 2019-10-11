from django.shortcuts import render
from .models import Product
from categories.models import Categories
from itertools import chain
from django.core.paginator import Paginator 
from django.shortcuts import get_object_or_404
from customers.models import Customer

def shop(request):
    if 'refrences' in request.GET:
        if 'A to Z' in request.GET['refrences']:
            products_list= Product.objects.order_by('title').filter(is_public = True)
        if 'Z to A' in request.GET['refrences']:    
            products_list= Product.objects.order_by('-title').filter(is_public = True)
        if 'low to high' in request.GET['refrences']:
            products_list= Product.objects.order_by('price').filter(is_public = True)
        if 'high to low' in request.GET['refrences']:    
            products_list= Product.objects.order_by('-price').filter(is_public = True)
    else:
        products_list= Product.objects.order_by('-release_time').filter(is_public = True)
            
    code1 = Categories.objects.get(categori_name = 'Men')
    code2 = Categories.objects.get(categori_name = 'Women')
    code3 = Categories.objects.get(categori_name = 'Children')
    paginator = Paginator(products_list, 6 )
    page = request.GET.get('page')
    products = paginator.get_page(page)
    context = {
        'products' : products,
        'menSize' :len(products_list.filter(categorie = code1)),
        'womenSize' :len(products_list.filter(categorie = code2)),
        'childrenSize' :len(products_list.filter(categorie = code3)),
        'values' : request.GET

    }
    if request.user.is_authenticated:
        customer = Customer.objects.get( user = request.user )
        context = {
            'products' : products,
            'menSize' :len(products_list.filter(categorie = code1)),
            'womenSize' :len(products_list.filter(categorie = code2)),
            'childrenSize' :len(products_list.filter(categorie = code3)),
            'values' : request.GET,
            'cart_size' : len(customer.cart.orders.all()),
        }
    return render(request,'shop/shop.html' ,context)

def men(request):
    products_list = Product.objects.order_by('-release_time').filter(is_public = True)
    code1 = Categories.objects.get(categori_name = 'Men')
    code2 = Categories.objects.get(categori_name = 'All')
    code3 = Categories.objects.get(categori_name = 'Women')
    code4 = Categories.objects.get(categori_name = 'Children')
    
    products= products_list.exclude(categorie = code3)
    products= products.exclude(categorie = code4)
    paginator = Paginator(products, 6 )
    page = request.GET.get('page')
    products = paginator.get_page(page)
    context = {
        'products' : products,
        'menSize' :len(products_list.filter(categorie = code1)),
        'womenSize' :len(products_list.filter(categorie = code3)),
        'childrenSize' :len(products_list.filter(categorie = code4)),
    }
    if request.user.is_authenticated:
        customer = Customer.objects.get( user = request.user )
        context = {
            'products' : products,
            'menSize' :len(products_list.filter(categorie = code1)),
            'womenSize' :len(products_list.filter(categorie = code3)),
            'childrenSize' :len(products_list.filter(categorie = code4)),
            'cart_size' : len(customer.cart.orders.all()),
        }
    return render(request,'shop/shop.html' ,context)

def women(request):
    products_list = Product.objects.order_by('-release_time').filter(is_public = True)
    code1 = Categories.objects.get(categori_name = 'Women')
    code2 = Categories.objects.get(categori_name = 'All') 
    code3 = Categories.objects.get(categori_name = 'Men')
    code4 = Categories.objects.get(categori_name = 'Children')   
    products= products_list.exclude(categorie = code3)
    products= products.exclude(categorie = code4)
    paginator = Paginator(products, 6 )
    page = request.GET.get('page')
    products = paginator.get_page(page)
    context = {
        'products' : products,
        'menSize' :len(products_list.filter(categorie = code3)),
        'womenSize' :len(products_list.filter(categorie = code1)),
        'childrenSize' :len(products_list.filter(categorie = code4)),
    }
    if request.user.is_authenticated:
        customer = Customer.objects.get( user = request.user )
        context = {
            'products' : products,
            'menSize' :len(products_list.filter(categorie = code3)),
            'womenSize' :len(products_list.filter(categorie = code1)),
            'childrenSize' :len(products_list.filter(categorie = code4)),
            'cart_size' : len(customer.cart.orders.all()),
        }
    return render(request,'shop/shop.html' ,context)

def children(request):
    products_list = Product.objects.order_by('-release_time').filter(is_public = True)
    code1 = Categories.objects.get(categori_name = 'Children')
    code2 = Categories.objects.get(categori_name = 'All')    
    code3 = Categories.objects.get(categori_name = 'Women')
    code4 = Categories.objects.get(categori_name = 'Men')

    products= products_list.exclude(categorie = code3)
    products= products.exclude(categorie = code4)
    paginator = Paginator(products, 6 )
    page = request.GET.get('page')
    products = paginator.get_page(page)

    context = {
        'products' : products,
        'menSize' :len(products_list.filter(categorie = code4)),
        'womenSize' :len(products_list.filter(categorie = code3)),
        'childrenSize' :len(products_list.filter(categorie = code1)),
    }
    if request.user.is_authenticated:
        customer = Customer.objects.get( user = request.user )
        context = {
            'products' : products,
            'menSize' :len(products_list.filter(categorie = code4)),
            'womenSize' :len(products_list.filter(categorie = code3)),
            'childrenSize' :len(products_list.filter(categorie = code1)),   
            'cart_size' : len(customer.cart.orders.all()),
        }
    return render(request,'shop/shop.html' ,context)

def product(request,product_id):
    product = get_object_or_404(Product,pk=product_id)
    context = {
        'product' : product ,
    }
    if request.user.is_authenticated:
        customer = Customer.objects.get( user = request.user )
        context = {
            'product' : product,
            'cart_size' : len(customer.cart.orders.all()),
        }
    return render(request,'shop/product.html' , context )

def search(request):
    if 'keyword' in request.GET :
        keyword = request.GET['keyword']
        products = Product.objects.filter(description__icontains = keyword)
        paginator = Paginator(products, 6 )
        page = request.GET.get('page')
        products = paginator.get_page(page)
        context ={
                'products' : products,
            }
        if request.user.is_authenticated:
            customer = Customer.objects.get( user = request.user )
            context = {
                'products' : products,
                'cart_size' : len(customer.cart.orders.all()),
            }    
        return render(request , 'shop/shop.html', context)