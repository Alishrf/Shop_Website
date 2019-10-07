from django.shortcuts import render ,redirect
from .options import countries
from customers.models import Customer
from django.contrib.auth.models import User
from .models import SubmittedOrder
from carts.models import Cart 
from django.contrib import messages


def checkout(request):
    if User.is_authenticated:
        customer = Customer.objects.get( user = request.user )
        context = {
            'customer' : customer ,
            'countries' : countries ,
        }
        return render(request , 'checkout/checkout.html',context)

def addSubmittedOrder(request):
    if request.method =='POST':
        id_cart = request.POST['id_cart']
        cart = Cart.objects.get(id = id_cart)
        for order in cart.orders.all() :
            if order.size == 'Large':
                if order.product.quantity_large >= order.quantity:
                    order.product.quantity_large = order.product.quantity_large - order.quantity
                    order.product.save()
                else :
                    messages.error(request,'Sorry ' + order.product.title + ' is not Available')
                    return redirect('dashboard') 

            if order.size == 'Medium':
                if order.product.quantity_medium >= order.quantity:
                    order.product.quantity_medium = order.product.quantity_medium - order.quantity
                    order.product.save()
                else :
                    messages.error(request , 'Sorry ' + order.product.title + ' is not Available')
                    return redirect('dashboard')
                    
            if order.size == 'Small':
                if order.product.quantity_small >= order.quantity:
                    order.product.quantity_small = order.product.quantity_small - order.quantity
                    order.product.save()
                else :
                    messages.error(request ,'Sorry ' + order.product.title + ' is not Available')
                    return redirect('dashboard')
            if order.size == 'Extra Large':
                if order.product.quantity_extralarge >= order.quantity:
                    order.product.quantity_extralarge = order.product.quantity_extralarge - order.quantity
                    order.product.save()
                else :
                    messages.error(request , 'Sorry ' + order.product.title + ' is not Available')
                    return redirect('dashboard')
        #######paaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaay  
        country = request.POST['country_name']
        first_name = request.POST['c_fname']
        last_name = request.POST['c_lname']
        if request.POST['c_companyname'] is not None:
            company_name = request.POST['c_companyname']
        else:
            company_name = ''
        address = request.POST['c_address']
        state = request.POST['c_state_country']
        posta = int(request.POST['c_postal_zip'])
        email = request.POST['c_email_address']
        phone = request.POST['c_phone']
        order_notes = request.POST['c_order_notes']
        submittedOrder = SubmittedOrder( country = country , first_name = first_name ,
         last_name =last_name , company_name =company_name ,address = address , state = state , posta = posta , email = email , phone = phone , order_notes = order_notes , cart = cart)

        submittedOrder.save()
        cart.orders.clear()
        cart.subtotal = 0
        cart.total = 0
        cart.save()
        messages.success(request,'Your Order Submitted Successfully')
        return redirect('index')

