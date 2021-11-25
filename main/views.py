from django.shortcuts import render

from product.models import Category, Product
from vendor.models import Vendor
from customermsg.models import messages
def HomePage(request):
    newest_products = Product.objects.all()
    mainVendors = Product.objects.all()
    categories = Category.objects.all()
    vendors = Vendor.objects.all()
    user_messages = messages.objects.all()
    return render(request,  'main/home_page.html',{'newest_products': newest_products,"mainVendors":mainVendors,'categories':categories, 'vendors':vendors,'user_messages':user_messages})
 