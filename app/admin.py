from django.contrib import admin
from .models import Customer, Product, Cart, OrderPlaced

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'locality', 'city', 'zipcode', 'state')
    verbose_name = "Customer"
    verbose_name_plural = "Customers"

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'selling_price', 'discounted_price', 'brand', 'category','product_image')
    verbose_name = "Product"
    verbose_name_plural = "Products"

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'quantity')
    verbose_name = "Cart"
    verbose_name_plural = "Carts"

@admin.register(OrderPlaced)
class OrderPlacedAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'customer', 'product', 'quantity', 'ordered_date', 'status')
    verbose_name = "Order Placed"
    verbose_name_plural = "Orders Placed"