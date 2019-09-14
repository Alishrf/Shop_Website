from django.shortcuts import render
from shop.models import Product
from realtor.models import Realtor
from django.contrib.auth.models import User

def index(request):
    return render(request,'pages/index.html')

def about(request):
    realtors = Realtor.objects.all()
    context = {
        'realtors' : realtors
    }
    return render(request,'pages/about.html',context)   