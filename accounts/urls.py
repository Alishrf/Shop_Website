from django.contrib import admin
from django.urls import path,include
from . import views 


urlpatterns = [
    path('register', views.register , name = 'register'),
    path('login', views.login , name = 'login'),
    path('dashboard', views.dashboard , name = 'dashboard'),
    path('logout', views.logout , name = 'logout'),
    path('addtocart', views.addToCart , name = 'addtocart'),
    path('removecart', views.removeCart , name = 'removecart'),
    path('addcoupon', views.addCoupon, name = 'addcoupon'),

]

