from django.urls import path
from shopping_cart.api.views import (
    ship_address, 
    bill_address, 
    Billing_addressCreateAPIView,
    Shipping_addressCreateAPIView,
    Shipping_addressRetrieveUpdateDestroyAPIView,
    Billing_addressRetrieveUpdateDestroyAPIView,
    OrderCreateAPIView,
    OrderItemCreateAPIView,
    OrderItemRetrieveUpdateDestroyAPIView,
    OrderRetrieveUpdateDestroyAPIView
    
    
    )


urlpatterns = [
    # path('shipping/', ship_address, name='ship_address'),
    path('shipping/', Shipping_addressCreateAPIView.as_view(), name='ship_address'),
    path('shipping/<int:pk>/', Shipping_addressRetrieveUpdateDestroyAPIView.as_view(), name='ship_address'),

    # path('billing/', bill_address, name='bill_address'),
    path('billing/', Billing_addressCreateAPIView.as_view(), name='bill_address'),
    path('billing/<int:pk>/', Billing_addressRetrieveUpdateDestroyAPIView.as_view(), name='bill_address'),

    path('orders/', OrderCreateAPIView.as_view(), name='orders'),
    path('orders-items/', OrderItemCreateAPIView.as_view(), name='order_items'),
    path('orders/items/<int:pk>/', OrderItemRetrieveUpdateDestroyAPIView.as_view(), name='order_item_update'),
    path('orders/<int:pk>/', OrderRetrieveUpdateDestroyAPIView.as_view(), name='order_update')


]
