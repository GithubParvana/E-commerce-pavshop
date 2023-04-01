from django.conf import settings
from django.shortcuts import render


# Create your views here.
def product_detail_page(request):
    return render(request, 'product-detail.html')
