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
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Department, Role,Topic 
from django.http import HttpResponse
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

def success(request):
    return render(request , 'success.html')


def token_send(request):
    return render(request , 'token_send.html')



def verify(request , auth_token):
    try:
        profile_obj = Profile.objects.filter(auth_token = auth_token).first()
    

        if profile_obj:
            if profile_obj.is_verified:
                messages.success(request, 'Your account is already verified.')
                return redirect('/accounts/login')
            profile_obj.is_verified = True
            profile_obj.save()
            messages.success(request, 'Your account has been verified.')
            return redirect('/accounts/login')
        else:
            return redirect('/error')
    except Exception as e:
        print(e)
        return redirect('/')

def error_page(request):
    return  render(request , 'error.html')







# def send_mail_after_registration(email , token):
#     subject = 'Your accounts need to be verified'
#     message = f'Hi paste the link to verify your account http://127.0.0.1:8000/verify/{token}'
#     email_from = settings.EMAIL_HOST_USER
#     recipient_list = [email]
#     send_mail(subject, message , email_from ,recipient_list )


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








from django.contrib.auth.models import User
from django.contrib import auth

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

from django.shortcuts import render
from django.core.paginator import Paginator 

from .models import Test

def quiz_test(request):
    test = Test.objects.all()

    test_paginator = Paginator(test, 1)

    page_num = request.GET.get('page')

    page = test_paginator.get_page(page_num)

    context = {
        'count' : test_paginator.count,
        'page' : page
    }
    return render(request, 'test.html', context)

def department(request):

    # departmentid = request.GET.get('department', None)
    # roleid = request.GET.get('role', None)
    # role = None
    # topic  = None
    # if departmentid:
    #     getdepartment = Department.objects.get(id=departmentid)
    #     role = Role.objects.filter(department=getdepartment)
    # if roleid:
    #        getrole = Role.objects.get(id=roleid)
    #        topic = Topic.objects.filter(Role=getrole)
    # department = Department.objects.all()
    # # if department is not None:    
    # #     departmentid = Department.objects.filter(id = 1)
    # #     roleid = Role.objects.filter(id = 1)
    # #     topic = Topic.objects.filter(id = 1)
    # #     return redirect('login/department/test1')
    return render(request, 'department.html')



def filter(request):

    results = request.GET['department']
    topics = request.GET['topic']
    roles = request.GET['role']
    return render(request,"departmentfilter.html",{'department':results,'topic':topics,'role':roles})

    

def testaccounts(request):
    testaccount = Testaccount.objects.all()

    testaccount_paginator = Paginator(testaccount, 1)

    page_num = request.GET.get('page')

    page = testaccount_paginator.get_page(page_num)

    context = {
        'count' : testaccount_paginator.count,
        'page' : page
    }
    return render(request, 'testaccounts.html', context)
    
def testsales(request):
    testsale = Testsale.objects.all()

    testsale_paginator = Paginator(testsale, 1)

    page_num = request.GET.get('page')

    page = testsale_paginator.get_page(page_num)

    context = {
        'count' : testsale_paginator.count,
        'page' : page
    }
    return render(request, 'testsales.html', context)
    

    

