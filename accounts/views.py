from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from carts.models import Cart
from customers.models import Customer
from coupon.models import Coupon
from orders.models import Order
from shop.models import Product
from datetime import datetime




def register(request):
    if request.POST:
        name = request.POST['c_fname']
        family_name = request.POST['c_lname']
        email = request.POST['c_email']
        password1 = request.POST['c_password']
        password2 = request.POST['c_password2']
        if password1==password2 :
            has_email = User.objects.filter(email = email)
            if has_email:
                messages.error(request,'This Email Already Use')   
                return  redirect(register)
            else:
                coupon = Coupon()
                coupon.save()
                cart = Cart(coupon = coupon , total = 0 , subtotal= 0)
                cart.save()

                user = User.objects.create_user(first_name = name , last_name = family_name ,
                 email = email , password = password1,username = email )

                customer = Customer(user = user , cart = cart)
                customer.save()
                messages.success(request , 'You Are Registered Successfully')
                return redirect(login)
        else :
            messages.error(request,'Your Passwords Aren\'t Match')   
            return  redirect(register)
    return render(request , 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['c_email']
        password = request.POST['c_password']
        user = auth.authenticate(username = email , password = password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'You Are Loged In Successfully')
            return redirect(dashboard)
        else:
            messages.error(request,'Email Or Passsword Is Not Availabe')
            return redirect(login)


    return render(request , 'accounts/login.html')

def dashboard(request):
    if User.is_authenticated:
        customer = Customer.objects.get(user= request.user)
        context = {
            'customer' : customer ,
        }
        return render(request , 'accounts/dashboard.html',context)

def addToCart(request):
    if request.method == 'POST':
        customer = Customer.objects.get(user= request.user)
        quantity = request.POST['quantity']
        size = request.POST['shop-sizes']
        product = Product.objects.get(pk = request.POST['product_id'])
        total_price = int(quantity) * float(product.price)
        order = Order(quantity = quantity , size = size  , product = product , total_price = total_price)
        order.save()
        customer.cart.orders.add(order)
        cart = customer.cart
        cart.subtotal = cart.subtotal + total_price
        cart.total = float(cart.subtotal) * int(100 - cart.coupon.off)/(100) 
        cart.save()
        

    return redirect('dashboard')

def removeCart(request):
    if request.method == 'POST':
        customer = Customer.objects.get(user= request.user)
        order = Order.objects.get(pk = request.POST['order_id'])
        cart = customer.cart
        cart.subtotal = cart.subtotal - order.total_price
        cart.total = float(cart.subtotal) * int(100 - cart.coupon.off)/(100) 
        cart.save() 
        customer.cart.orders.remove(order)
        order.delete() 
        messages.success(request , 'Order Removed Successfully')

    return redirect('dashboard')


def addCoupon(request):
    if request.method == 'POST':
        customer = Customer.objects.get(user= request.user)
        cart = customer.cart
        coupon = Coupon.objects.get(code = request.POST['coupon_id'])
        if coupon is not None:
            present = datetime.date(datetime.now())
            d = datetime.date(coupon.expiration_date) 
            if  present <=  d:
                cart.coupon = coupon
                cart.coupon.save()
                cart.total = float(cart.subtotal) * int(100 - cart.coupon.off)/(100) 
                cart.save()
                messages.success(request , 'Coupon Id Accepted Successfully')
            else:    
                messages.error(request ,'Your Coupon IS Expired')    

        else:
            messages.error(request ,'Your Coupon Code Is Not Valid')    

    return redirect('dashboard')    


def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        messages.success(request,'You Are Now Logged Out')

    return redirect('login')    