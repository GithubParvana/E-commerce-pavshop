from django.urls import path

from checkout import views


urlpatterns = [
    path('checkout/', views.checkout_page, name='checkout_page'),
]
