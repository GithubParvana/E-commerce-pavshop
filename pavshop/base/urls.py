from django.urls import path

from base import views


urlpatterns = [
    path('base/', views.base_page, name='base_page'),
]
