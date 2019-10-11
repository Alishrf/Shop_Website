from django.contrib import admin
from .models import Cart

class CartAdmin(admin.ModelAdmin):
    list_display = ( 'id','total')
    search_fields= ( 'id' ,)
    list_per_page = 10
    
admin.site.register(Cart,CartAdmin)
