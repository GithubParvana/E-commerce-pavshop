from django.urls import path

from contact import views


urlpatterns = [
    path('contact/', views.contact_page, name='contact_page'),
]
