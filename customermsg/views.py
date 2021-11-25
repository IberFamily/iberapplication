from django.shortcuts import redirect, render
from customermsg.forms import sendUsMessage
from customermsg.models import messages
def MessageUs(request):
    
    if request.method == 'POST':
        form = sendUsMessage(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_msg')
    else:
        form = sendUsMessage()
    context =  {'form':form}
    return render(request, 'customermsg/messages.html',context)

def displayMessages(request):
    user_messages = messages.objects.all()
    return render(request, 'customermsg/display_messages.html',{'user_messages':user_messages})

def success_msg(request):
    return render(request, 'customermsg/success_msg.html')