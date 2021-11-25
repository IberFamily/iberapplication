from django import forms
from django.db.models.fields import TimeField
from django.forms import ModelForm
from django.forms.utils import to_current_timezone


from product.models import Product
from order.models import OrderItem

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['category','vendor', 'title', 'description','slug', 'price', 'image',]

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['status']


class Create_new_User_and_vendor(forms.Form):
    name = forms.IntegerField()
    title = forms.IntegerField()
    phone = forms.IntegerField()
    location = forms.IntegerField()
    delivery = forms.IntegerField()
    work_hours = forms.IntegerField()
    open_close_status = forms.CheckboxInput()
    images = forms.ImageField()
    vendor_baner = forms.ImageField()
    created_at = forms.TimeField()
    created_by = forms.CharField()
 
               