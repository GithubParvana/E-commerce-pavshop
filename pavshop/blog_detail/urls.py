from django.urls import path
from blog_detail import views   # this is a convenient way to import views;

# --- we can write like below:  ---

# import blog_detail.views  - using dot(.), we can import views here;
# from . import views  - can cause some conflicts in project, may not find the folder;
# from blog_detail import *   - we may import all from the app's views.py file;


urlpatterns = [
    path('blog_detail/', views.blog_detail_page, name='blog_detail_page'),
]
