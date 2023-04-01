from django.conf import settings
from django.shortcuts import render



# Create your views here.
def about_us_page(request):
    return render(request, 'about-us.html')

