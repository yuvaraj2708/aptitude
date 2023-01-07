from django.contrib import admin
from django.urls import path
from .views import *
from django.conf.urls.static import static
urlpatterns = [
    path('' , login_attempt , name="login_attempt"),
    path('register/' , register_attempt , name="register_attempt"),
    path('login/test1/' , quiz_test , name="test"),
    path('login/test1/import/', simple_upload,name="import"),
    path('login/' ,  home  , name="home"), 
    path('token/' , token_send , name="token_send"),
    path('success/' , success , name='success'),
    path('verify/<auth_token>' , verify , name="verify"),
    path('error' , error_page , name="error"),
    path('hrlogin/' , hrlogin , name="login"),
    path('hrlogin/dashboard/' , dashboard , name="dashboard"),
    path('hrregister/' , hrregister , name="registration"),
    ]
