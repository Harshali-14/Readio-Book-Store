from rest_framework import serializers
from shop.models import Category, Book, Cart, OrderItem, Order, Wishlist, Rating


# ---------------- CATEGORY ----------------
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


# ---------------- BOOK ----------------
class BookSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Book
        fields = '__all__'


# ---------------- CART ----------------
class CartSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()
    book_details = BookSerializer(source='book', read_only=True)

    class Meta:
        model = Cart
        fields = '__all__'
        read_only_fields = ['user']

    def get_total_price(self, obj):
        return obj.book.price * obj.quantity


# ---------------- ORDER ITEM ----------------
class OrderItemSerializer(serializers.ModelSerializer):
    book_details = BookSerializer(source='book', read_only=True)

    class Meta:
        model = OrderItem
        fields = '__all__'
        read_only_fields = ['order']


# ---------------- ORDER ----------------
class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True, source='orderitem_set')

    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['user', 'total_amount']

# ---------------- WISHLIST ----------------
class WishlistSerializer(serializers.ModelSerializer):
    book_details = BookSerializer(source='book', read_only=True)

    class Meta:
        model = Wishlist
        fields = '__all__'
        read_only_fields = ['user']

    def to_representation(self, instance):
        """Better output format"""
        data = super().to_representation(instance)
        return data


# ---------------- RATING ----------------
class RatingSerializer(serializers.ModelSerializer):
    book_details = BookSerializer(source='book', read_only=True)

    class Meta:
        model = Rating
        fields = '__all__'
        read_only_fields = ['user']

    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Rating must be between 1 and 5")
        return value