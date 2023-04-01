from django.urls import path

from blog_list import views


urlpatterns = [
    path('blog_list/', views.blog_list_page, name='blog_list_page'),
]
