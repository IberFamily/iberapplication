from django.urls import path
from . import views


urlpatterns = [
    path('paneladmin', views.adminWatchPanel, name="adminPanel"),

]
