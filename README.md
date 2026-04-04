# Readio — Online Bookstore

Readio is a web-based online bookstore application built using Django.  
It provides a complete system for browsing books, managing a cart, and processing secure payments through Razorpay.

---

## Project Overview

Readio is designed to simulate a real-world e-commerce bookstore platform with secure authentication, payment processing, and a user-friendly interface.

---

## Features

- User registration, login, and logout  
- Browse and view books  
- Detailed book pages  
- Add and remove books from cart  
- Cart total calculation  
- Razorpay payment integration  
- Secure payment verification  
- User order history  
- Responsive and modern UI  

---

## Technology Stack

- Backend: Django (Python)  
- Frontend: HTML, CSS, Bootstrap  
- Database: SQLite  
- Payment Gateway: Razorpay  
- Authentication: Django built-in authentication  

---

## Project Structure


bookstore/
│
├── shop/ Main Django application
│ ├── migrations/
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ └── admin.py
│
├── templates/ HTML templates
│
├── static/ Static files (CSS, JS, images)
│
├── bookstore/ Project configuration
│ ├── settings.py
│ ├── urls.py
│ ├── asgi.py
│ └── wsgi.py
│
├── db.sqlite3 SQLite database
├── manage.py Django management script
└── requirements.txt Project dependencies


---

## Installation

### Clone the repository


git clone https://github.com/Harshali-14/Readio-Book-Store

cd bookstore


---

### Create virtual environment


python -m venv venv


Activate:

**Windows**

venv\Scripts\activate


**Mac/Linux**

source venv/bin/activate


---

### Install dependencies


pip install -r requirements.txt


---

### Configure environment variables

Create `.env` file:


SECRET_KEY=your_secret_key
DEBUG=True
RAZORPAY_KEY_ID=your_key_id
RAZORPAY_KEY_SECRET=your_key_secret


---

### Run migrations


python manage.py makemigrations
python manage.py migrate


---

### Create superuser


python manage.py createsuperuser


---

### Run server


python manage.py runserver


Open in browser:

http://127.0.0.1:8000/


---

## Razorpay Integration

- Razorpay is used as the payment gateway  
- Payments are securely processed from backend  
- Payment verification is implemented using Razorpay signature  

---

## Security

- Sensitive data stored in environment variables  
- CSRF protection enabled  
- Secure authentication system  
- Payment verification implemented  

---

## Future Improvements

- Advanced search and filtering  
- Recommendation system  
- Allow users to add books

---

## Author

Harshali Kulkarni  
MCA Student  

---

