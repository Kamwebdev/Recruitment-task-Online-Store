from django.contrib import admin
from .models import Product, Order, Address, Cart

class ProductAdmin(admin.ModelAdmin):
    pass
admin.site.register(Product, ProductAdmin)

class AddressAdmin(admin.ModelAdmin):
    pass
admin.site.register(Address, AddressAdmin)

class CartInline(admin.StackedInline):
    model = Cart

class OrderAdmin(admin.ModelAdmin):
    inlines = [CartInline]

admin.site.register(Order, OrderAdmin)