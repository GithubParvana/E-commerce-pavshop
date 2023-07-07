from django.db import models
# from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
# from authentication.models import User

from djmoney.models.fields import MoneyField
from djmoney.money import Money
from djmoney.models.validators import MaxMoneyValidator, MinMoneyValidator
from djmoney.contrib.exchange.models import convert_money

from django_countries.fields import CountryField

from base.models import AbstractModel

from django.core.validators import MinValueValidator, MaxValueValidator

from products.models import *

from django.contrib.auth import get_user_model

User = get_user_model()


DIRECT_BANK_TRANSFER = "direct bank transfer"
CASH_ON_DELIVERY = "cash on delivery"
CHEQUE_PAYMENT = "cheque payment"
PAYPAL = "paypal"


CHOICES = (
    (DIRECT_BANK_TRANSFER, "Direct Bank Transfer"),
    (CASH_ON_DELIVERY, "Cash On Delivery"),
    (CHEQUE_PAYMENT, "Cheque Payment"),
    (PAYPAL, "Paypal"),
)




# checkout page ucun: 2 form

class Shipping_address(AbstractModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=255)
    address = models.TextField()
    country = CountryField(blank_label="(select country)")
    city = models.CharField(max_length=255)
    phone = PhoneNumberField()
    
    
    
    def __str__(self):
        return '{} {} {} {}'.format(self.user, self.company, self.address, self.city)


    def user_name(self):
        return self.user.get_full_name()




# Create your models here.  - BillShipInfo modeli
class Billing_address(AbstractModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=255)
    address = models.TextField()
    country = CountryField(blank_label="(select country)")
    city = models.CharField(max_length=255)
    phone = PhoneNumberField()
    shipping_address = models.ForeignKey(Shipping_address, on_delete=models.CASCADE, null=True, blank=True)
    
    

    # class Meta:
    #     verbose_name = "Billing_address"
    #     verbose_name_plural = "Billing_addresses"


    def __str__(self):
        return '{} {} {} {} {}'.format(self.user, self.company, self.address, self.city, self.shipping_address)


    def user_name(self):
        return self.user.get_full_name()





# Order
class Order(AbstractModel):
    STATUS_CHOICES = (
        (1, 'Ordered'),
        (2, 'Shipped'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders', null=True, blank=True)
    status = models.CharField(max_length=255, choices = STATUS_CHOICES, default=1, blank=True, null=True)
    transaction_id = models.CharField(max_length=100, null=True, blank=True)



    def user_name(self):
        return self.request.user.get_full_name()
   
    
    def __str__(self):
        return '{} {}'.format(self.user, self.transaction_id)


    # def user_name(self):
    #     return self.request.user.get_full_name()



# Order item
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items', null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True, related_name='order_items')
    quantity = models.IntegerField(default=0, null=True, blank=True)
   
    

    def __str__(self):
        return '{} {} {}'.format(self.quantity, self.product, self.order)
    










# class Cart(AbstractModel):
#     cart_number = models.IntegerField()
#     cvv_code = models.IntegerField()
#     expiration_date = models.DateTimeField()
#     member = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)


#     def __str__(self):
#         return '{} {} {} {}'.format(self.cart_number, self.cvv_code, self.expiration_date, self.member)
    





class Coupon(AbstractModel):
    name = models.CharField(max_length=50)   # yaz endirimi
    code = models.IntegerField()           # 1094
    discount = models.IntegerField()         # 20
    is_percent = models.BooleanField()            
    is_active = models.BooleanField()


    def __str__(self):
        return '{} {} {} {} {}'.format(self.name, self.code, self.discount, self.is_percent, self.is_active)



# class Order(AbstractModel):
#     STATUS = (
#         (1, 'Pending'),
#         (2, 'Order Confirmed'),
#         (3, 'Out for Delivery'),
#         (4, 'Delivered'),
#     )

#     # customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
#     basket = models.ForeignKey(Basket, on_delete=models.CASCADE, related_name='orders')

#     status = models.IntegerField(choices=STATUS, default=1, null=True, blank=True)
#     # sub_total = models.IntegerField()   # endirimsiz total; endirim olanda ise onu views.py da hesablayacagiq;
    
#     # product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE, related_name='orders')
   


#     def __str__(self):
#         return '{} {} {}'.format(self.status, self.coupon, self.basket)
