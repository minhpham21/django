from django.db import models
from product.models import Variation
from user.models import CustomerUser

# Create your models here.
# Quantity      : Số lượng

#GIỎ HÀNG
class Cart (models.Model):
    user = models.ForeignKey (CustomerUser, on_delete = models.CASCADE)
    created = models.DateTimeField (auto_now_add = True)
    update = models.DateTimeField (auto_now = True)

# MỤC HÀNG
class CartItem (models.Model):
    cart = models.ForeignKey (Cart, on_delete = models.CASCADE)
    item = models.ForeignKey (Variation, on_delete = models.CASCADE)
    quantity = models.IntegerField (default = 0)

