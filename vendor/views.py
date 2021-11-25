import os
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import UpdateView
from customermsg.models import messages
from order.models import Order, OrderItem
from django.core.mail import send_mail
from .models import Vendor
from product.models import Category
from .forms import Create_new_User_and_vendor, ProductForm,OrderItemForm
from django.conf import settings
from cart.forms import CheckoutForm
from django.contrib.auth.models import User


def CreateVendor(request):
   
    return render(request, 'vendor/create_vendor.html')
    
@login_required
def vendor_admin(request):
    vendor = request.user.vendor
    products = vendor.products.all()
    orders = vendor.orders.all()
    user_messages = messages.objects.all()
    
        
    for order in orders:
        order.vendor_amount = 0
        order.vendor_paid_amount = 0
        order.fully_paid = True

        for item in order.items.all():
            if item.vendor == request.user.vendor:
                if item.vendor_paid:
                    order.vendor_paid_amount += item.get_total_price()
                else:
                    order.vendor_amount += item.get_total_price()
                    order.fully_paid = False

    return render(request, 'vendor/vendor_admin.html', {'vendor': vendor, 'products': products, 'orders': orders,'user_messages':user_messages})

@login_required
def UpdateStatusOrder(request,pk):
    status = OrderItem.objects.get(id=pk)
    form = OrderItemForm(instance=status)
    
    if request.method == 'POST':
        form = OrderItemForm(request.POST, instance=status)
        if form.is_valid():
            form.save()
            subject = "Iber Donosi Sve!"
            message = f"Pozdrav {status.order.first_name} , Hvala na poverenju! objekat < {status.vendor} > je prihvatio vašu porudzbinu. Očekivano vreme dostave na adresu {status.order.address} je 40 do 60 minuta. IBER"
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [status.order.email]
            send_mail(subject,message,from_email,recipient_list,fail_silently=False)
            return redirect('vendor_admin')
        else:
            status = OrderItemForm()
    context = {'status':status,'form':form}
    return render(request, 'vendor/order_form.html',context)


@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            product = form.save(commit=False)
            product.vendor = request.user.vendor
            product.slug = slugify(product.title)
            product.save()

            return redirect('vendor_admin')
    else:
        form = ProductForm()
    
    return render(request, 'vendor/add_product.html', {'form': form})


def vendors(request):
    vendors = Vendor.objects.all()

    return render(request, 'vendor/vendors.html', {'vendors': vendors})

def vendor(request, vendor_id):
    vendor = get_object_or_404(Vendor, pk=vendor_id)

    return render(request, 'vendor/vendor.html', {'vendor': vendor})


