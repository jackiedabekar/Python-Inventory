from django.contrib import admin
from .models import Customer, Product, Order, OrderItem, ShippingAddress

admin.site.register(ShippingAddress)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
    )

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'price',
        'active',
        'quantity',
        'image',
    )
    list_editable = ('price','active', 'quantity')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'customer',
        'date_order',
        'complete',
    )
    list_editable = ('complete',)

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'product',
        'order',
        'quantity'
    )
