from django.shortcuts import render

# Create your views here.

def admin_dashboard(request):
    return render(request,'ADMINTEMP/admin_dashboard.html')


def homepage(request):
    return render(request,'Modified_files/HOMEPAGE.html')


def loginpage(request):
    return render(request,'Modified_files/LOGINPAGE.html')