from django.contrib import admin
from django.urls import path
from .views import *
from .views import BookApiView
from django.conf.urls.static import static
from rest_framework import routers
urlpatterns = [
    path('',rules,name="rules"),
    path('login/' , login_attempt , name="login_attempt"),
    path('register/' , register_attempt , name="register_attempt"),
    path('department/test1/import/', simple_upload,name="import"),
    path('hrlogin/' , login , name="login"),
    path('hrregister/' , signup , name="registration"),
    path('hrlogin/dashboard/' , dashboard , name="dashboard"),
    path('login/department/' , department , name="department"),
    path('filter/' , filter , name="filter"),
    path('add/addrecord/', addrecord, name='addrecord'),
    path('add/', add, name='addrecord'),
    path('result/', result, name='result'),
    
    ]


rout = routers.SimpleRouter()
rout.register('api',BookApiView,basename="api")
urlpatterns += rout.urls
