from django.contrib import admin
from django.urls import path
from .views import *
from django.conf.urls.static import static
urlpatterns = [
    path('',rules,name="rules"),
    path('login/' , login_attempt , name="login_attempt"),
    path('register/' , register_attempt , name="register_attempt"),
    # path('login/department/test1/' , quiz_test , name="test"),
    # path('department/testaccounts/' , testaccounts , name="testaccount"),
    # path('department/testsales/' , testsales , name="testsale"),
    # path('department/test1/import/', simple_upload,name="import"),
    # path('hrlogin/' , login , name="login"),
    # path('hrregister/' , signup , name="registration"),
    # path('hrlogin/dashboard/' , dashboard , name="dashboard"),
    path('login/department/' , department , name="department"),
    path('login/department/filter' , filter , name="filter"),
    ]
