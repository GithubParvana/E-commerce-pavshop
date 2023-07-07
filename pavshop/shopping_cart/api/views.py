from shopping_cart.models import Shipping_address, Billing_address, Order, OrderItem
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from shopping_cart.api.serializers import (
    Shipping_addressSerializer, 
    Billing_addressSerializer, 
    Shipping_addressCreateSerializer,
    Billing_addressCreateSerializer,
    OrderSerializer,
    OrderCreateSerializer,
    OrderItemSerializer,
    OrderItemCreateSerializer,
    OrderItemUpdateSerializer
    )


# rest framework -> function-based
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView





# # GET
# def ship_address(request):
#     shipping_list = Shipping_address.objects.all()
#     serializer = Shipping_addressSerializer(shipping_list, many = True)
#     return JsonResponse(data=serializer.data, safe=False)




# POST 
class Billing_addressCreateAPIView(CreateAPIView):
    serializer_class = Billing_addressCreateSerializer


# # GET  - gerek urls.py da elave bir route yaradaq, o da hansi yuxarida ise o isleyecek, elverisli deyil get ve post ucun API ayri yazmaq
# class Billing_addressCreateAPIView(ListAPIView):
#     serializer_class = Billing_addressCreateSerializer
#     queryset = Billing_address.objects.all()



# GET ve POST -> 2-sini birlesdiren bir API View var
class Billing_addressCreateAPIView(ListCreateAPIView):
    serializer_class = Billing_addressCreateSerializer
    queryset = Billing_address.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)



# DELETE ve UPDATE(PUT VE PATCH) -> 2-sini birlesdiren bir API View var
class Billing_addressRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = Billing_addressSerializer
    queryset = Billing_address.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)







# POST 
class Shipping_addressCreateAPIView(CreateAPIView):
    serializer_class = Shipping_addressCreateSerializer


# # GET  - gerek urls.py da elave bir route yaradaq, o da hansi yuxarida ise o isleyecek, elverisli deyil get ve post ucun API ayri yazmaq
# class Shipping_addressCreateAPIView(ListAPIView):
#     serializer_class = Shipping_addressCreateSerializer
#     queryset = Shipping_address.objects.all()



# GET ve POST -> 2-sini birlesdiren bir API View var
class Shipping_addressCreateAPIView(ListCreateAPIView):
    serializer_class = Shipping_addressCreateSerializer
    queryset = Shipping_address.objects.all()



# DELETE ve UPDATE(PUT VE PATCH) -> 2-sini birlesdiren bir API View var
class Shipping_addressRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = Shipping_addressSerializer
    queryset = Shipping_address.objects.all()




# GET ve POST @api_views ile
@api_view(http_method_names=['GET', 'POST'])
def ship_address(request):
    if request.method == 'POST':
        serializer = Shipping_addressCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, safe=False, status = 201, context={'request' : request})
        return JsonResponse(data=serializer.errors, safe=False, status = 400)
    shipping_list = Shipping_address.objects.all()
    serializer = Shipping_addressSerializer(shipping_list, context={'request' : request}, many = True)
    return JsonResponse(data=serializer.data, safe=False)







# GET ve POST @api_views ile
@api_view(http_method_names=['GET', 'POST'])
def bill_address(request):
    if request.method == 'POST':
        serializer = Billing_addressCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, safe=False, status = 201, context={'request' : request})
        return JsonResponse(data=serializer.errors, safe=False, status = 400)
    billing_list = Billing_address.objects.all()
    serializer = Billing_addressSerializer(billing_list, context={'request' : request}, many = True)
    return JsonResponse(data=serializer.data, safe=False)





# GET ve POST -> 2-sini birlesdiren bir API View var
class OrderCreateAPIView(ListCreateAPIView):
    serializer_class = OrderCreateSerializer
    queryset = Order.objects.all()



# DELETE ve UPDATE(PUT VE PATCH) -> 2-sini birlesdiren bir API View var
class OrderRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = OrderCreateSerializer
    queryset = Order.objects.all()
    # permission_classes = (IsAuthenticatedOrReadOnly,)




# GET ve POST -> 2-sini birlesdiren bir API View var
class OrderItemCreateAPIView(ListCreateAPIView):
    serializer_class = OrderItemCreateSerializer
    queryset = OrderItem.objects.all()



# DELETE ve UPDATE(PUT VE PATCH) -> 2-sini birlesdiren bir API View var
class OrderItemRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = OrderItemUpdateSerializer
    queryset = OrderItem.objects.all()
    # permission_classes = (IsAuthenticatedOrReadOnly,)


















# class OrderGetView(RetrieveUpdateDestroyAPIView):
#     serializer_class = OrderSerializer
#     queryset = Order.objects.all()




# class OrderItemUpdateView(RetrieveUpdateDestroyAPIView):
#     serializer_class = OrderItemUpdateSerializer
#     queryset = OrderItem.objects.all()

