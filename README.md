# 📚 Readio — Online Bookstore

Readio is a web-based online bookstore application developed using Django.  
It provides a complete e-commerce platform where users can browse books, manage carts, place orders, and make secure online payments using Razorpay.

---

# 🚀 Features

- User Registration & Login
- Secure Authentication System
- Browse Available Books
- Book Detail Pages
- Add to Cart / Remove from Cart
- Cart Total Calculation
- Razorpay Payment Gateway Integration
- Secure Payment Verification
- Order History Management
- Wishlist Feature
- Responsive UI Design
- Admin Panel for Management

---

# 🛠️ Technology Stack

| Technology | Description |
|------------|-------------|
| Python | Backend Programming Language |
| Django | Web Framework |
| HTML/CSS | Frontend Structure & Styling |
| Bootstrap | Responsive UI |
| SQLite | Database |
| Razorpay | Payment Gateway |
| Django Authentication | User Authentication System |

---

# 📂 Project Structure

```bash
bookstore/
│
├── bookstore/                 # Main Project Configuration
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── shop/                      # Main Application
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── static/                    # Global Static Files
│
├── templates/                 # HTML Templates
│
├── db.sqlite3                 # SQLite Database
├── manage.py                  # Django Management Script
├── requirements.txt           # Project Dependencies
└── README.md                  # Project Documentation
```

---

# ⚙️ Installation Guide

## 1️⃣ Clone Repository

```bash
git clone https://github.com/Harshali-14/Readio-Book-Store.git

cd bookstore
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 Environment Variables

Create a `.env` file in the root directory and add:

```env
SECRET_KEY=your_secret_key
DEBUG=True

RAZORPAY_KEY_ID=your_key_id
RAZORPAY_KEY_SECRET=your_key_secret
```

---

# 🗃️ Apply Database Migrations

```bash
python manage.py makemigrations

python manage.py migrate
```

---

# 👤 Create Superuser

```bash
python manage.py createsuperuser
```

---

# ▶️ Run Development Server

```bash
python manage.py runserver
```

Open in browser:

```bash
http://127.0.0.1:8000/
```

---

# 💳 Razorpay Integration

- Secure online payment system
- Razorpay checkout integration
- Backend payment verification
- Signature verification implemented
- Order payment status management

---

# 🔒 Security Features

- CSRF Protection Enabled
- Secure Authentication System
- Environment Variable Protection
- Secure Payment Verification
- Django Built-in Security Features

---

# 📸 Screenshots

## 🏠 Homepage
![Homepage](static/screenshots/bookstore.png)

## 🔐 Login Page
![Login](static/screenshots/login.png)

## 📝 Register Page
![Register](static/screenshots/register.png)

## 🛒 Cart Page
![Cart](static/screenshots/cart.png)

## 💳 Checkout Page
![Checkout](static/screenshots/checkout.png)

## 💰 Razorpay Payment
![Razorpay](static/screenshots/razorpay.png)

## ⏳ Payment Processing
![Processing](static/screenshots/payment_processing.png)

## ✅ Payment Success
![Success](static/screenshots/payment_success.png)

## 📦 Order Tracking
![Tracking](static/screenshots/order_tracking.png)

## 📚 Orders
![Orders](static/screenshots/orders.png)

## 👤 User Profile
![Profile](static/screenshots/profile.png)

## ❤️ Wishlist
![Wishlist](static/screenshots/wishlist.png)

---

# 🌟 Future Improvements

- Advanced Search & Filters
- Book Recommendation System
- Multiple Payment Methods
- User Reviews & Ratings
- Email Notifications
- Admin Analytics Dashboard

---

# 👩‍💻 Author

**Harshali Kulkarni**  
MCA Student  
Django & Python Developer

---

# 📄 License

This project is developed for educational purposes.