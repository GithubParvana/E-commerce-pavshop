from django.conf import settings
from django.shortcuts import render


# Create your views here.
def blog_list_page(request):
    return render(request, 'blog-list.html')
