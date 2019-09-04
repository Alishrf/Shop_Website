from django.contrib import admin
from django.urls import path,include
from . import views



urlpatterns = [
    path('', views.shop , name = 'shop'),
    path('men', views.men , name = 'men'),
    path('children', views.children , name = 'children'),
    path('women', views.women , name = 'women'),
    path('products/<int:product_id>', views.product , name = 'product'),

]