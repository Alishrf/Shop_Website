from django.contrib import admin
from .models import Order

class AdminOrder(admin.ModelAdmin):
    list_display = ('id','product' , 'size' , 'quantity' , 'total_price')
    list_display_links = ('id','product')
    search_fields = ('id' , )

admin.site.register(Order , AdminOrder)