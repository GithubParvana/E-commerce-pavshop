from django.contrib import admin

from .models import *


class Billing_addressAdmin(admin.ModelAdmin):
    list_display = ('user', 'company', 'address', 'country', 'city', 'phone')



class Shipping_addressAdmin(admin.ModelAdmin):
    list_display = ('user', 'company', 'address', 'country', 'city', 'phone')



class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('quantity', 'product', 'order')



class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'status', 'transaction_id')


# class CartAdmin(admin.ModelAdmin):
#     list_display = ('cart_number', 'cvv_code', 'expiration_date', 'member')


class CouponAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'discount', 'is_percent', 'is_active')






# Register your models here.
admin.site.register(Billing_address, Billing_addressAdmin)
admin.site.register(Shipping_address, Shipping_addressAdmin)

admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Coupon, CouponAdmin)
# admin.site.register(Order, OrderAdmin)
