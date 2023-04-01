from django.conf import settings
from django.shortcuts import render


# Create your views here.
def shopping_cart_page(request):
    return render(request, 'shopping-cart.html')
