from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages


# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request,'home.html',{'products': products})

def about(request):
    return render(request,'about.html')

def login_user(request):
    if request.method =='POST':
        username = request.POST('username')
        password = request.POST('password')
        user = authenticate(request, username=username, password = password)
        if user is not None:
            login(request,user)
            messages.success(request("You Have Been Loged In"))
            return redirect('home')
        else:
            messages.success(request("There Was An Error, Please Try Again"))
            return redirect('login') 
         
    else:
        return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('home')
