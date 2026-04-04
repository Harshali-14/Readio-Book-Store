from django.contrib import admin
from .models import Book, Category, Cart, Order, OrderItem

# Basic registrations
admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Cart)

# Inline for Order Items
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

# Order Admin
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'total_amount', 'status', 'created_at']
    inlines = [OrderItemInline]

# Register models
admin.site.register(Order, OrderAdmin)