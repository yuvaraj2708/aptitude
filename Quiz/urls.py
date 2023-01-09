from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.log,name="Home"),
    path("register/",views.reg,name="registerpage"),
    path("depart/",views.department,name="departmentpage"),
    path("test/",views.Test,name="testpage"),
]

admin.site.index_title = 'Margy Site Administration'
