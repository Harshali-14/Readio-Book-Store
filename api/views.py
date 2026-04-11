from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import *
from api.serializers import *


# ---------------- CATEGORY ----------------
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# ---------------- BOOK ----------------
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# ---------------- CART ----------------
class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# ---------------- ORDER ----------------
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()   # ✅ ADD THIS

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        user = self.request.user
        cart_items = Cart.objects.filter(user=user)

        if not cart_items.exists():
            raise serializers.ValidationError("Cart is empty")

        total = sum(item.book.price * item.quantity for item in cart_items)

        order = serializer.save(user=user, total_amount=total)

        OrderItem.objects.bulk_create([
            OrderItem(
                order=order,
                book=item.book,
                quantity=item.quantity,
                price=item.book.price
            )
            for item in cart_items
        ])

        cart_items.delete()
# ---------------- WISHLIST ----------------
class WishlistViewSet(viewsets.ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Wishlist.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# ---------------- RATING ----------------
class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Rating.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)