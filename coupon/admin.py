from django.contrib import admin
from .models import Coupon

class AdminCoupon(admin.ModelAdmin):
    list_display = ('id' , 'code' , 'off' , 'expiration_date' ,)
    list_display_links = ('id','code')
    search_fields = ('code' ,)


admin.site.register(Coupon , AdminCoupon)