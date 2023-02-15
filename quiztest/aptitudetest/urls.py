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
    path('hrlogin/' , login , name="login"),
    path('hrregister/' , signup , name="registration"),
    path('hrlogin/dashboard/' , dashboard , name="dashboard"),
    # path('login/department/' , department , name="department"),
    path('login/filter/' , filter , name="filter"),
   
      ]


rout = routers.SimpleRouter()
rout.register('api',BookApiView,basename="api")
urlpatterns += rout.urls
