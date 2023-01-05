from multiprocessing import AuthenticationError
from django.shortcuts import  render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import NewUserForm
from .models import login


# def homepage(request):
# Create your views here.
def log(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        conn =authenticate(request,username=username,password=password)
    
        if conn is not None:
           login(request,conn)           
           return redirect("/test")     

        else:
             messages.success(request,'Invalid username or password.')
             return redirect("/")
    else:
        return render(request,'login.html',{})

def reg(request):

    if request.method == "POST":
       form= NewUserForm(request.POST)
       if form.is_vaild():
          user = form.save()
          login(request,conn)
          messages.success(request,"Registration successfull.")
       else:
             return redirect("Home")
    else:
         messages.error(request,"Unsccessful registration. Invalid information.")
         form = NewUserForm()
         return render(request , 'register.html')
    

def test(request):
    return render(request,'Test.html')

