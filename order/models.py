from django.db import models
from user.models import CustomerUser
from cart.models import Cart

# Create your models here.
# Quantity      : Số lượng

#ĐẶT HÀNG
class Order (models.Model):
    user = models.ForeignKey (CustomerUser, on_delete = models.CASCADE)
    car = models.ForeignKey (Cart, on_delete = models.CASCADE)
    address_ship = models.CharField (default = '', max_length = 255)
    order_description = models.TextField (default = '', max_length = '')
    completed = models.BooleanField (default = False)   