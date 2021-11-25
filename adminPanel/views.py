from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User
from customermsg.models import messages
from vendor.models import Vendor 
from order.models import Order
from django.contrib.admin.views.decorators import staff_member_required


def adminWatchPanel(request):
    users = User.objects.all()
    orders = Order.objects.all()
    user_messages = messages.objects.all()
    context = {'users': users,'orders':orders,'user_messages':user_messages}
    return render (request, 'adminPanel/adminpanel.html',context)

def vendor(request,vendor_id):
    vendor = get_object_or_404(Vendor,pk=vendor_id)
    return render(request, 'vendor/vendor.html',{'vendor':vendor})
