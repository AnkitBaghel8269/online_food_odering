from datetime import datetime
from django.db import models
from restaurant.models import OurMenu
# from accounts.models import Register
# Create your models here.
class CustomerUser(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contect_number = models.CharField(max_length=50)
    address = models.TextField(max_length=200)
    
    def __str__(self):
        return self.first_name


class Order(models.Model):
    user  = models.ForeignKey(CustomerUser, on_delete=models.CASCADE,related_name='user')
    product = models.ForeignKey(OurMenu, on_delete=models.CASCADE,related_name='product')
    product_qty = models.IntegerField(null=False,blank=False)
    datetime = models.DateTimeField(auto_now_add=True)


class ContectUs(models.Model):
    first_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    massege = models.TextField(max_length=200)
    
    def __str__(self):
        return self.first_name

