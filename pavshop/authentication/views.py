from django.conf import settings
from django.shortcuts import render



# Create your views here.
def login_page(request):
    return render(request, 'login.html')


# Create your views here.
def register_page(request):
    return render(request, 'register.html')
