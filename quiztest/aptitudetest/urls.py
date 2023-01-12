from django.contrib import admin
from django.urls import path
from .views import *
from django.conf.urls.static import static
urlpatterns = [
    
    path('' , login_attempt , name="login_attempt"),
    path('register/' , register_attempt , name="register_attempt"),
    path('department/test1/' , quiz_test , name="test"),
    path('department/testaccounts/' , testaccounts , name="testaccount"),
    path('department/testsales/' , testsales , name="testsale"),
    path('department/test1/import/', simple_upload,name="import"),
    path('department/hrlogin/' , login , name="login"),
    path('department/hrregister/' , signup , name="registration"),
    path('hrlogin/dashboard/' , dashboard , name="dashboard"),
    path('department/' , department , name="department"),
    ]
