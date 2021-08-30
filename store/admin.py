from django.contrib import admin
from .models import Customer, Product, Order, OrderItem, ShippingAddress

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)

# @admin.register(Customer)
# class CustomerAdmin(admin.ModelAdmin):
#     list_display = (
#         'id',
#         'user',
#         'name',
#         'email'
#     )

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = (
#         'id',
#         'name',
#         'price',
#         'digital',
#         # 'product_quantity',
#         'image',
#     )
#     list_editable = ('price',)

# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     list_display = (
#         'id',
#         'customer',
#         'date_order',
#         'complete',
#         'transaction_id'
#     )
#     list_editable = ('customer', 'complete')

# @admin.register(OrderItem)
# class OrderItemAdmin(admin.ModelAdmin):
#     list_display = (
#         'id',
#         'product',
#         'order',
#         'quantity'
#     )

# @admin.register(ShippingAddress)
# class ShippingAddressAdmin(admin.ModelAdmin):
#     list_display = (
#         'id',
#         'customer',
#         'order',
#         'address',
#         'city',
#         'state',
#         'zipcode'
#     )