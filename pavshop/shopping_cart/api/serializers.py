from rest_framework import serializers
from shopping_cart.models import Shipping_address, Billing_address, Order, OrderItem
from products.apis.serializers import ProductSerializer

# GET
class Shipping_addressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipping_address
        fields = (
            'id',
            # 'user',
            'user_name',
            'company',
            'address',
            'country',
            'city',
            'phone'
        )


# POST
class Shipping_addressCreateSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Shipping_address
        fields = (
            'id',
            'user',
            'company',
            'address',
            'country',
            'city',
            'phone'
        )


    def validate(self, attrs):
        request = self.context['request']
        attrs['user'] = request.user
        return super().validate(attrs)



# GET
class Billing_addressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Billing_address
        fields = (
            'id',
            # 'user',
            'user_name',
            'company',
            'address',
            'country',
            'city',
            'phone',
            'shipping_address'
        )



# POST
class Billing_addressCreateSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Billing_address
        fields = (
            'id',
            'user',
            'company',
            'address',
            'country',
            'city',
            'phone',
            'shipping_address'
        )

    def validate(self, attrs):
        request = self.context['request']
        attrs['user'] = request.user
        return super().validate(attrs)



# GET
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = (
            'id',
            # 'user',
            'user_name',
            # 'complete',
            'transaction_id'
        )



# POST
class OrderCreateSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Order
        fields = (
            'id',
            'user',
            # 'complete',
            'transaction_id'
        )


    def validate(self, attrs):
        request = self.context['request']
        attrs['user'] = request.user
        return super().validate(attrs)



# GET
class OrderItemSerializer(serializers.ModelSerializer):
    product = serializers.CharField(source='product.title')
    class Meta:
        model = OrderItem
        fields = (
            'product',
            'order',
            'quantity',

        )



# POST
class OrderItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = (
            'product',
            'order',
            'quantity',

        )



class OrderItemUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = (
            'id',
            'product',
            'order',
            'quantity'
        )
