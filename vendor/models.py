from django.contrib.auth.models import User
from django.db import models

class Vendor(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255 , null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    delivery = models.CharField(max_length=255,  null=True, blank=True)
    work_hours = models.CharField(max_length=255,  null=True, blank=True)
    open_close_status = models.BooleanField(default=False,  null=True, blank=True)
    images = models.ImageField(upload_to='uploads/', blank=True, null=True)
    vendor_baner = models.ImageField(upload_to='uploads/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.OneToOneField(User, related_name='vendor', on_delete=models.CASCADE)
    
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name