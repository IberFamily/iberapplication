from django.urls import path
from . import views

urlpatterns = [ 
    path('messages', views.MessageUs, name="messages"),
    path('displayMessages',views.displayMessages, name="displayMessages"),
    path('success_msg', views.success_msg, name="success_msg"),
]