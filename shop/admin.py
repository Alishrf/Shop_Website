from django.contrib import admin
from .models import Product


class ShopAdmin(admin.ModelAdmin):
    list_display = ('id','title','price','is_public')
    list_display_links =('id','title')
    list_per_page = 12
    list_filter = ('price','is_public','quantity_medium')
    search_fields = ('title','price','description')



admin.site.register(Product,ShopAdmin)