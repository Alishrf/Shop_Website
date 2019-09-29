from django.contrib import admin
from .models import Cart

class CartAdmin(admin.ModelAdmin):
    search_fields= ( 'id' ,)

admin.site.register(Cart,CartAdmin)
