from django.conf import settings
from django.shortcuts import render


# Create your views here.
def checkout_page(request):
    return render(request, 'checkout.html')
