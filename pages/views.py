from django.shortcuts import render
from shop.models import Product
from realtor.models import Realtor

def index(request):
    return render(request,'pages/index.html')

def about(request):
    realtors = Realtor.objects.all()
    context = {
        'realtors' : realtors
    }
    return render(request,'pages/about.html',context)   