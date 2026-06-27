# Readio — Django Online Book Store

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge\&logo=python)
![Django](https://img.shields.io/badge/Django-5.x-darkgreen?style=for-the-badge\&logo=django)
![Django REST Framework](https://img.shields.io/badge/Django_REST_Framework-API-red?style=for-the-badge)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple?style=for-the-badge\&logo=bootstrap)
![SQLite](https://img.shields.io/badge/SQLite-Database-blue?style=for-the-badge\&logo=sqlite)
![Razorpay](https://img.shields.io/badge/Razorpay-Payment-0C6CF2?style=for-the-badge)

A modern Online Book Store developed using Django with authentication, shopping cart, wishlist, order management, Razorpay payment integration, and REST APIs.

</div>

---

# Overview

Readio is a full-stack Online Book Store built with Django. It allows users to browse books, add books to their shopping cart or wishlist, place orders, and complete secure online payments through Razorpay.

The project also includes REST APIs developed using Django REST Framework for backend communication and future frontend/mobile application integration.

---

# Features

## User Authentication

* User Registration
* User Login
* User Logout
* Secure Password Authentication
* User Profile Management

## Book Management

* Browse Books
* View Book Details
* Category-wise Listing
* Responsive Book Catalog

## Shopping Cart

* Add Books to Cart
* Update Quantity
* Remove Books
* Automatic Total Calculation

## Wishlist

* Add Books to Wishlist
* Remove Wishlist Items
* Move Wishlist Items to Cart

## Payment

* Razorpay Payment Gateway
* Secure Payment Verification
* Checkout Process
* Payment Success & Failure Handling

## Orders

* Place Orders
* View Order History
* Track Orders
* Payment Status

## REST API

* Django REST Framework
* JSON Responses
* CRUD Operations
* Thunder Client Tested

## User Interface

* Bootstrap 5
* Mobile Responsive
* Clean Navigation
* User-Friendly Design

---

# Technology Stack

| Technology            | Purpose                   |
| --------------------- | ------------------------- |
| Python                | Backend                   |
| Django                | Web Framework             |
| Django REST Framework | REST API                  |
| HTML5                 | Frontend                  |
| CSS3                  | Styling                   |
| Bootstrap 5           | Responsive Design         |
| JavaScript            | Client-side Functionality |
| SQLite                | Database                  |
| Razorpay              | Payment Gateway           |
| Thunder Client        | API Testing               |

---

# Project Structure

```text
Readio-Django-Online-Book-Store/
│
├── bookstore/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── shop/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── api_views.py
│   ├── urls.py
│   ├── forms.py
│   └── admin.py
│
├── templates/
├── static/
│   └── screenshots/
├── media/
├── db.sqlite3
├── manage.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/Harshali-14/Readio-Django-Online-Book-Store.git

cd Readio-Django-Online-Book-Store
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the project root.

```env
SECRET_KEY=your_secret_key

DEBUG=True

RAZORPAY_KEY_ID=your_key_id

RAZORPAY_KEY_SECRET=your_key_secret
```

---

# Database Setup

Run migrations.

```bash
python manage.py makemigrations

python manage.py migrate
```

---

# Create Superuser

```bash
python manage.py createsuperuser
```

---

# Run the Project

```bash
python manage.py runserver
```

Open your browser:

```
http://127.0.0.1:8000/
```

---

# REST API

## Available Endpoints

| Method | Endpoint        | Description      |
| ------ | --------------- | ---------------- |
| GET    | `/api/books/`   | List Books       |
| GET    | `/api/cart/`    | View Cart        |
| GET    | `/api/orders/`  | Order History    |
| POST   | `/api/payment/` | Razorpay Payment |

### API Features

* JSON Response
* REST Architecture
* CRUD Operations
* Thunder Client Tested
* Mobile App Ready

---

# Payment Integration

Readio integrates Razorpay to provide secure online payment processing.

### Payment Flow

```
Browse Books
      │
      ▼
Add to Cart
      │
      ▼
Checkout
      │
      ▼
Razorpay Payment
      │
      ▼
Payment Verification
      │
      ▼
Order Confirmation
```

---

# Security

* Django Authentication
* Password Hashing
* CSRF Protection
* Session Management
* Environment Variables
* Razorpay Signature Verification
* Django Built-in Security Middleware

---

# Screenshots

## Homepage

<img src="static/screenshots/bookstore.png" width="900">

---

## Login

<img src="static/screenshots/login.png" width="900">

---

## Register

<img src="static/screenshots/register.png" width="900">

---

## Book Details

<img src="static/screenshots/book_details.png" width="900">

---

## Shopping Cart

<img src="static/screenshots/cart.png" width="900">

---

## Wishlist

<img src="static/screenshots/wishlist.png" width="900">

---

## Checkout

<img src="static/screenshots/checkout.png" width="900">

---

## Razorpay Payment

<img src="static/screenshots/razorpay.png" width="900">

---

## Payment Processing

<img src="static/screenshots/payment_processing.png" width="900">

---

## Payment Success

<img src="static/screenshots/payment_success.png" width="900">

---

## Orders

<img src="static/screenshots/orders.png" width="900">

---

## Order Tracking

<img src="static/screenshots/order_tracking.png" width="900">

---

## User Profile

<img src="static/screenshots/profile.png" width="900">

---

# Future Improvements

* Advanced Search
* Book Reviews & Ratings
* Email Notifications
* Coupon & Discount System
* Inventory Management
* Admin Analytics Dashboard
* Multiple Payment Methods
* PostgreSQL Support
* Docker Deployment
* Cloud Deployment
* Mobile Application

---

# Contributing

Contributions are welcome.

1. Fork the repository.

2. Create a new branch.

```bash
git checkout -b feature-name
```

3. Commit your changes.

```bash
git commit -m "Add new feature"
```

4. Push the branch.

```bash
git push origin feature-name
```

5. Create a Pull Request.

---

# Requirements

```
Python 3.10+

Django

Django REST Framework

Bootstrap 5

SQLite

Razorpay

python-dotenv
```

---

# Author

**Harshali Kulkarni**

MCA Student

Python & Django Developer

GitHub: https://github.com/Harshali-14


---

# License

This project is developed for educational and learning purposes.

---

If you found this project useful, please consider starring the repository.
