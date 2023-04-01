from django.urls import path

from . import views


urlpatterns = [
    path('', views.shopping_cart_page, name='shopping_cart_page'),
]
