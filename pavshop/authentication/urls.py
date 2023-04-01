# this python module has been designed for app URLs. That is called informally URLconf;
from django.urls import path

from authentication import views


urlpatterns = [
    path('register/', views.register_page, name='register_page'),
    path('login/', views.login_page, name='login_page'),
]

