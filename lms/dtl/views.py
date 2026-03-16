from django.shortcuts import render
from django.utils import timezone

def shopping_cart(request):
    context = {
        "customer": "Chinedu",
        "cart_items": [
            {"name": "Laptop", "price": 250000, "quantity": 1},
            {"name": "Headphones", "price": 15000, "quantity": 2},
            {"name": "USB Cable", "price": 2000, "quantity": 3},
        ],
        "has_discount": True,
        "store": {
            "name": "Tech World",
            "city": "Abuja",
        },
        "today": timezone.now(),
    }
    return render(request, "dtl/cart.html", context)