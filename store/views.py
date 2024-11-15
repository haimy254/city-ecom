from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from .form import*
from django.contrib.auth.forms import UserCreationForm
# from django import form


# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request,'home.html',{'products': products})

def category(request,foo):
    #replace gyphens with space
    foo = foo.replace('-',' ')

    try:
        #look up the category
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(request, 'category.html', {'products':products, 'category': category})
    except:
        return redirect('home')
    

def product(request,pk):
    product = Product.objects.get(id=pk)
    return render(request,'product.html',{'product': product})

def about(request):
    return render(request,'about.html')

def login_user(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password = password)
        if user is not None:
            login(request,user)
            # messages.success(request("You Have Been Loged In"))
            return redirect('home')
        else:
            messages.success(request("There Was An Error, Please Try Again"))
            return redirect('login') 
         
    else:
        return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('home')


def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            #log in user 
            user = authenticate(username = username, password = password)
            login(request,user)
            return redirect('home')
        else:
            # messages.success(request("Whoops, There was a problem, Please try again"))
            return redirect('register')
    else:
        return render(request, 'register.html', {'form': form})
