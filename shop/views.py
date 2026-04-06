from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Cart, Order, OrderItem
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Category
from .models import Wishlist
from .models import Rating
from django.db.models import Avg
from .models import Book, Rating
import razorpay
from django.conf import settings
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from django.http import HttpResponse
from django.contrib.auth import update_session_auth_hash
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import hmac
import hashlib
from django.contrib.auth.decorators import login_required
import json
from django.http import JsonResponse
from nltk.tokenize import word_tokenize
import random
from .logic import get_recommendation

def verify_payment(order_id, payment_id, signature):
    generated_signature = hmac.new(
        key=settings.RAZORPAY_KEY_SECRET.encode(),
        msg=f"{order_id}|{payment_id}".encode(),
        digestmod=hashlib.sha256
    ).hexdigest()

    return generated_signature == signature

# 🔐 Register
def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('register')

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(request, "Account created successfully! Please login.")
        return redirect('login')

    return render(request, 'shop/register.html')


# 🔐 Login
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials")

    return render(request, 'shop/login.html')


# 🔓 Logout

def logout_view(request):
    logout(request)
    return redirect('login')


# 🏠 Home
def home(request):
    books = Book.objects.all()
    query = request.GET.get('q')
    category = request.GET.get('category')

    if query:
        books = books.filter(title__icontains=query)

    if category:
        books = books.filter(category__name=category)

    categories = Category.objects.all()

    return render(request, 'shop/home.html', {
        'books': books,
        'categories': categories
    })

@login_required
@csrf_exempt
def chatbot(request):
    if request.method == "POST":
        data = json.loads(request.body)
        message = data.get("message", "").lower()

        words = word_tokenize(message)

        books = Book.objects.all()

        # 🎯 SMART RECOMMENDATION
        if any(word in ["recommend", "suggest", "books"] for word in words):

            # Category filter
            for cat in Category.objects.all():
                if cat.name.lower() in message:
                    books = books.filter(category=cat)

            # Keyword filter
            if "python" in words:
                books = books.filter(title__icontains="python")
            elif "django" in words:
                books = books.filter(title__icontains="django")
            elif "web" in words:
                books = books.filter(title__icontains="web")

            books = books[:5]

            if books.exists():
                reply = "📚 Recommended Books:\n"
                for b in books:
                    reply += f"- {b.title} (₹{b.price})\n"
            else:
                reply = random.choice([
                    "🤔 Try different keywords.",
                    "📖 Try 'recommend python books'.",
                    "🔍 No matching books found."
                ])

        # 👋 Greetings
        elif any(word in ["hello", "hi", "hey"] for word in words):
            reply = "👋 Hello! I can suggest books for you."

        # 📦 Orders
        elif "order" in words:
            reply = "📦 Go to 'My Orders' to track your orders."

        # ❓ Default
        else:
            reply = random.choice([
                "🤖 Try: 'Recommend Python books'",
                "📚 Ask me for book suggestions!",
                "🔍 I can help you find books."
            ])

        return JsonResponse({"reply": reply})
    
@csrf_exempt
def chatbot_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        message = data.get("message")

        reply = get_recommendation(message)

        return JsonResponse({"reply": reply})    

# 📖 Book Detail
@login_required
def book_detail(request, id):
    book = get_object_or_404(Book, id=id)

    # ⭐ Handle POST actions (Rating OR Add to Cart)
    if request.method == "POST":

        # ⭐ Rating
        if 'rating' in request.POST:
            if request.user.is_authenticated:
                rating_value = request.POST.get('rating')

                Rating.objects.update_or_create(
                    user=request.user,
                    book=book,
                    defaults={'rating': rating_value}
                )

                messages.success(request, "⭐ Rating submitted successfully!")
            else:
                messages.warning(request, "Please login to rate this book.")

        # 🛒 Add to Cart
        elif 'add_to_cart' in request.POST:
            messages.success(request, "🛒 Book added to cart!")

            # 👉 Later you will add Cart model logic here

        return redirect('book_detail', id=id)

    # ⭐ Average Rating
    avg_rating = Rating.objects.filter(book=book).aggregate(
        Avg('rating')
    )['rating__avg']

    # ⭐ Total Reviews
    total_reviews = Rating.objects.filter(book=book).count()

    # ⭐ Related Books (same category)
    related_books = Book.objects.filter(
        category=book.category
    ).exclude(id=book.id)[:4]

    return render(request, 'shop/book_detail.html', {
        'book': book,
        'avg_rating': avg_rating,
        'total_reviews': total_reviews,
        'related_books': related_books
    })

# 🛒 Add to Cart
@login_required
def add_to_cart(request, id):
    book = get_object_or_404(Book, id=id)

    cart_item, created = Cart.objects.get_or_create(
        user=request.user,
        book=book
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')


# 🛒 Cart Page
@login_required
def cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    total = sum(item.total_price() for item in cart_items)

    return render(request, 'shop/cart.html', {
        'cart_items': cart_items,
        'total': total
    })


# ❌ Remove from Cart
@login_required
def remove_from_cart(request, id):
    item = get_object_or_404(Cart, id=id, user=request.user)
    item.delete()
    return redirect('cart')


# ➕ Increase Quantity
@login_required
def increase_quantity(request, id):
    item = get_object_or_404(Cart, id=id, user=request.user)
    item.quantity += 1
    item.save()
    return redirect('cart')


# ➖ Decrease Quantity
@login_required
def decrease_quantity(request, id):
    item = get_object_or_404(Cart, id=id, user=request.user)

    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()

    return redirect('cart')


# 💳 Checkout
@login_required
def checkout(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.book.price for item in cart_items)

    amount = int(total_price * 100)  # paisa

    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

    payment = client.order.create({
        "amount": amount,
        "currency": "INR",
        "payment_capture": "1"
    })

    return render(request, 'shop/checkout.html', {
        'cart_items': cart_items,
        'total_price': total_price,
        'payment': payment,
        'RAZORPAY_KEY_ID': settings.RAZORPAY_KEY_ID
    })

@login_required
def add_to_wishlist(request, id):
    book = get_object_or_404(Book, id=id)

    Wishlist.objects.get_or_create(user=request.user, book=book)
    return redirect('wishlist')


@login_required
def wishlist(request):
    items = Wishlist.objects.filter(user=request.user)
    return render(request, 'shop/wishlist.html', {'items': items})


@login_required
def remove_from_wishlist(request, id):
    item = get_object_or_404(Wishlist, id=id, user=request.user)
    item.delete()
    return redirect('wishlist')

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'shop/order_history.html', {'orders': orders})

@login_required
def track_order(request, id):
    order = get_object_or_404(Order, id=id)
    return render(request, 'shop/track_order.html', {'order': order})

def cancel_order(request, id):
    order = get_object_or_404(Order, id=id, user=request.user)

    if request.method == 'POST':
        if order.status in ['Pending', 'Shipped']:
            order.status = 'Cancelled'
            order.save()
            messages.success(request, "Order cancelled successfully!")
        else:
            messages.error(request, "Order cannot be cancelled at this stage.")

    return redirect('order_history')

@csrf_exempt
def payment_success(request):
    user = request.user

    cart_items = Cart.objects.filter(user=user)

    if not cart_items.exists():
        return render(request, 'shop/order_success.html', {'order': None})

    total_amount = sum(item.book.price for item in cart_items)

    order = Order.objects.create(
        user=user,
        total_amount=total_amount,
        payment_id=request.GET.get('payment_id', 'N/A'),
        paid=True
    )

    for item in cart_items:
        OrderItem.objects.create(
            order=order,
            book=item.book,
            quantity=1,
            price=item.book.price
        )

    cart_items.delete()

    return redirect('order_success', order_id=order.id)

from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from django.http import HttpResponse

def invoice(request, order_id):
    order = Order.objects.get(id=order_id)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="invoice_{order.id}.pdf"'

    doc = SimpleDocTemplate(response)
    styles = getSampleStyleSheet()

    elements = []

    elements.append(Paragraph(f"Invoice - Order #{order.id}", styles['Title']))
    elements.append(Paragraph(f"Total: ₹{order.total_amount}", styles['Normal']))  # ✅ FIXED

    for item in order.items.all():
        elements.append(Paragraph(f"{item.book.title} - ₹{item.price}", styles['Normal']))

    doc.build(elements)

    return response
@login_required
def profile(request):
    return render(request, 'shop/profile.html')

@login_required
def edit_profile(request):
    user = request.user

    if request.method == "POST":
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.save()
        return redirect('profile')

    return render(request, 'shop/edit_profile.html')
@login_required
def change_password(request):
    if request.method == 'POST':
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']

        user = request.user

        # ✅ Check current password
        if not user.check_password(current_password):
            messages.error(request, "Current password is incorrect!")
            return redirect('change_password')

        # ❌ Prevent empty password
        if not new_password:
            messages.error(request, "New password cannot be empty!")
            return redirect('change_password')

        # ✅ Update password
        user.set_password(new_password)
        user.save()

        # ✅ Keep user logged in
        update_session_auth_hash(request, user)

        messages.success(request, "Password updated successfully!")
        return redirect('profile')

    return render(request, 'shop/change_password.html')

def order_success(request, order_id):
    order = Order.objects.get(id=order_id)

    return render(request, 'shop/order_success.html', {
        'order': order
    })