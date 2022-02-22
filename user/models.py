from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
# Address : Địa chỉ
    
# USER NGƯỜI DÙNG
class CustomerUser (AbstractUser):
    address = models.CharField (default = '', max_length = 255)
    phone = models.CharField (default = '', max_length = 15)