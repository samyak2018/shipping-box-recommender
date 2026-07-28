# Shipping Box Recommendation System

A Django-based application that recommends the most suitable shipping box for an order based on product dimensions, total volume, weight capacity, box availability, and cost.

## Features

- Create orders using products from the product catalogue
- Specify quantities for multiple products
- Calculate total order weight automatically
- Calculate total order volume automatically
- Validate individual product dimensions against shipping boxes
- Support product rotation when checking dimensions
- Filter inactive shipping boxes
- Reject boxes with insufficient weight capacity
- Reject boxes with insufficient volume
- Select the cheapest valid shipping box
- Use the smallest box as a tie-breaker when costs are equal
- Display order summary and recommended box
- Manage products and shipping boxes through Django Admin
- Automated tests for recommendation logic, forms, and views
- Responsive Django template UI

## Technology Stack

- Python
- Django
- SQLite
- HTML
- CSS
- Django Templates
- Django Test Framework

## Project Structure

```text
box-recommender/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── orders/
│   ├── migrations/
│   │
│   ├── services/
│   │   └── box_recommender.py
│   │
│   ├── static/
│   │   └── orders/
│   │       └── css/
│   │           └── style.css
│   │
│   ├── templates/
│   │   └── orders/
│   │       ├── base.html
│   │       ├── order_create.html
│   │       └── order_detail.html
│   │
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── manage.py
├── requirements.txt
├── README.md
└── .gitignore