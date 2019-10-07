from django.contrib import admin
from django.urls import path,include
from . import views 
from accounts.views import addCoupon


urlpatterns = [
    path('', views.checkout , name = 'checkout'),
    path('addsubmittedorder', views.addSubmittedOrder , name = 'addSubmittedOrder'),
    path('addcoupon', addCoupon , name = 'addcoupon'),



]