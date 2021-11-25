from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields import CharField, UUIDField, related
import uuid

from product.models import Product
from vendor.models import Vendor
import os
from twilio.rest import Client



class Order(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    paid_amount = models.DecimalField(max_digits=8, decimal_places=2)
    vendors = models.ManyToManyField(Vendor, related_name='orders')
    created_by = models.OneToOneField(User, related_name='order', on_delete=models.CASCADE, null=True, blank=True)
   
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.first_name
        
  
        
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, related_name='items', on_delete=models.CASCADE)
    vendor_paid = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    quantity = models.IntegerField(default=1)
    created_by = models.OneToOneField(User, related_name='OrderItem', on_delete=models.CASCADE, null=True, blank=True)
    order_number = models.UUIDField(default=uuid.uuid4, unique=True, db_index=True, editable=False)
    
    STATUS_ORDER= (
        ('Na Čekanju','Na čekanju'),
        ('Prihvaćeno','Prihvaćeno'),
        ('Spremnjeno','Spremnjeno'),
        ('Odbijeno','Odbijeno')
    ) 
    status = models.CharField(max_length=200,choices=STATUS_ORDER,default='Na čekanju')
    
    def __str__(self):
        return '%s' % self.id
    
    def get_total_price(self):
        return self.price * self.quantity

  