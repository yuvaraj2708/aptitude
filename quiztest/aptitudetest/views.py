from aptitudetest.models import Profile
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
import uuid
from .models import Profile
from .resources import PersonResource
from tablib import Dataset
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,EmptyPage
from django.shortcuts import render
from .models import Department, Role,Topic 
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.


# def home(request):
#     return render(request , 'home.html')
def rules(request):
    return render(request,'rules_and_regulations.html')

@login_required
def login_attempt(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

      
        user = authenticate(username = username , password = password)
        print(f'user {user}')
        if user is not None:
             login(request)
             return redirect('/login/department')
        else:
           
          messages.error(request, 'Wrong password.')
          return redirect('/')

    return render(request , 'login.html')


    
   
def register_attempt(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(password)

        try:
            if User.objects.filter(username = username).first():
                messages.success(request, 'Username is taken.')
                return redirect('/register')

            if User.objects.filter(email = email).first():
                messages.success(request, 'Email is taken.')
                return redirect('/register')
            
            user_obj = User(username = username , email = email)
            user_obj.set_password(password)
            user_obj.save()
            auth_token = str(uuid.uuid4())
            profile_obj = Profile.objects.create(user = user_obj , auth_token = auth_token)
            profile_obj.save()
            (email , auth_token)
            return redirect('/')

        except Exception as e:
            print(e)


    return render(request , 'register.html')


def simple_upload(request):
    if request.method == 'POST':
        person_resource = PersonResource()
        dataset = Dataset()
        new_person = request.FILES['myfile']

        if not new_person.name.endswith('xlsx'):
            messages.info(request,'wrong format')
            return render(request,'upload.html')

        imported_data = dataset.load(new_person.read(),format='xlsx')
        for data in imported_data:
            value = Test(
        		data[0],
        		data[1],
        		data[2],
        		data[3],
                data[4],
                data[5],
                data[6],
                data[7],
                data[8],
                data[9]
        		)
        value.save()       
    return render(request,'upload.html')

def dashboard(request):
    return render(request,'mainhr.html')


def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                User.objects.get(username = request.POST['username'])
                return render (request,'register.html', {'error':'Username is already taken!'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                auth.login(request,user)
                return redirect('hrregister')
        else:
            return render (request,'hrregister.html', {'error':'Password does not match!'})
    else:
        return render(request,'hrregister.html')


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password = request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('dashboard/')
        else:
            return render (request,'hrlogin.html', {'error':'Username or password is incorrect!'})
    else:
        return render(request,'hrlogin.html')



def department(request):

   
    return render(request, 'department.html')



def filter(request):
    results = request.GET['department']
    topics = request.GET['topic']
    roles = request.GET['role']

    questions = Test.objects.filter(department=results, role=roles, topic=topics)
  
    test = Test.objects.all()

    test_paginator = Paginator(test, 21)

    page_num = request.GET.get('page')

    page = test_paginator.get_page(page_num)

  
   
   
    context = {
        'questions': questions,
        'department':results,
        'topic':topics,
        'role':roles,
        'count' : test_paginator.count,
        'page' : page,

        
    }
    return render(request,"departmentfilter.html", context)


    
   

