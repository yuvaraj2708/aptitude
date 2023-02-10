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
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from django.template import loader
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
    
    
    return render(request,"Department.html")

  
def filter(request):
   
    
    department=request.GET.get('department')
    role=request.GET.get('role')
    topic=request.GET.get('topic') 
    questions=  Test.objects.filter(department=department,role=role,topic=topic)

    book_paginator = Paginator(questions, 1)
    page_num = request.GET.get('page')
    page = book_paginator.get_page(page_num)
    
    if request.method == 'POST':
        print(request.POST)
        questions=Test.objects.filter(department=department,role=role,topic=topic)
        score=0
        wrong=0
        correct=0
        total=0
        for q_page in questions:
            total+=1
            print(request.POST.get(q_page.question))
            print(q_page.answeroption)
            print()
            if q_page.answeroption == request.POST.get(q_page.question):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        return render(request,'submit.html',context)
    else:
        questions=Test.objects.filter(department=department,role=role,topic=topic)
        context = {
            'questions':questions,
            'count': book_paginator.count,
            'page' : page 
        }
    
    return render(request,"departmentfilter.html",context)
 
   







    
class BookApiView(ModelViewSet):
    queryset = Test.objects.all()
    serializer_class=TestSerializer
    permission_class = [IsAuthenticated ] 








#    (department='IT', role='PYTHON', topic=' AWARENESS')
   
# (department='ACCOUNTS', role='ACCOUNTANT', topic='ACCOUNTANCY')
# (department='SALES', role='MARKETING', topic='PRODUCT AWARENESS')