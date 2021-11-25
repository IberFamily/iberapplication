from  django.contrib.auth import views as auth_views
from  django.urls import path
from . import views
import vendor
urlpatterns = [ 
   path('create_vendor/', views.CreateVendor, name="create_vendor"),
   path('vendor_admin/', views.vendor_admin, name="vendor_admin"),
   path('add_product/', views.add_product, name="add_product"),
   path('logout/', auth_views.LogoutView.as_view(), name='logout'),
   path('login/', auth_views.LoginView.as_view(template_name='vendor/login.html'), name="login"),
   path('/', views.vendors, name="vendors"),
   path('<int:vendor_id>/', views.vendor, name='vendor'),
   path('updateStatus<int:pk>/', views.UpdateStatusOrder, name="adminUpdate")
]