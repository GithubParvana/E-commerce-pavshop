from django.conf import settings
from django.shortcuts import render


# Create your views here.
def base_page(request):
    return render(request, 'base.html')
