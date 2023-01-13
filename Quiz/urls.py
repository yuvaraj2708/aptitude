from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.log,name="Home"),
    path("register/",views.reg,name="registerpage"),
    path("sample/",views.department,name="Dependant"),
    path("test/",views.Test,name="testpage"),
    path("depart/",views.sample,name="Sample")

   

]

admin.site.index_title = 'Margy Site Administration'
