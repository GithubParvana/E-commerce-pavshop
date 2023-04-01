from django.conf import settings
from django.shortcuts import render


# Create your views here.
def blog_detail_page(request):
    return render(request, 'blog-detail.html')
