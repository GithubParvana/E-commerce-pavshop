from django.urls import path

from . import views

urlpatterns = [
    path('', views.product_detail_page, name = 'product_detail_page'),
]