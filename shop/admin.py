from django.contrib import admin
from .models import Book, Category, Cart, Order, OrderItem, Wishlist, Rating

# 📚 Book Admin
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'price', 'category']
    search_fields = ['title', 'author']
    list_filter = ['category']

# 📂 Category Admin
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

# 🛒 Cart Admin
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'book', 'quantity']

# 📦 Inline Order Items
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

# 📦 Order Admin (UPGRADED)
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'total_amount', 'paid', 'status', 'created_at']
    list_filter = ['status', 'paid', 'created_at']
    search_fields = ['user__username', 'payment_id']
    inlines = [OrderItemInline]

# ❤️ Wishlist
@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ['user', 'book']

# ⭐ Rating
@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['user', 'book', 'rating']