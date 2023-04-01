from django.conf import settings
from django.shortcuts import render


# Create your views here.
def contact_page(request):
    return render(request, 'contact.html')
