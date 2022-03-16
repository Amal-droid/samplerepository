from django.urls import path

from vms_app import views

urlpatterns = [
    path('',views.homepage,name ='homepage'),
    path('loginpage/',views.loginpage,name ='loginpage'),
path('admin_dashboard/',views.admin_dashboard,name ='admin_dashboard'),
 ]