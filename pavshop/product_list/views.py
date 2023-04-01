from django.conf import settings
from django.shortcuts import render


# Create your views here.
def product_list_page(request):
    return render(request, 'product-list.html')
