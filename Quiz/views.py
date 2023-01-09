from multiprocessing import AuthenticationError
from django.shortcuts import  render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login 
from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.contrib.auth.models import User
from .models import login


# def homepage(request):
# Create your views here.
def log(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user =authenticate(request,username=username,password=password)
    
        if user is not None:
           login(request,user)            
           return redirect("/depart")     

        else:
             messages.success(request,'Invalid username or password.')
             return redirect("/")
    else:
        return render(request,'login.html',{})

def reg(request):

    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 =request.POST.get('password2')
       
        if password1 == password2:
             user =User.objects.create_user(request,username=name,email=email,password1=password2)
             user.is_staff = True
             user.is_active = True
             user.is_superuser =True
             user.save()
             messages.success(request,"Your account has been created ,you are able to login")
             return redirect("/")

        else:
            messages.warning(request,"Your account has been invalid!,So please enter the valid password")
            return redirect("/register")
    else:
        form = CreateUserForm()
        return render(request,"register.html",{'form':form})
      
            
    
def department(request):
    

      


    return render(request,'Depart.html')
def Test(request):
    return render(request,'Test.html')

