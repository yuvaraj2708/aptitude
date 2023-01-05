from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.log,name="Home"),
    path("register/",views.reg,name="register"),
    path("test/",views.test,name="Test")
]

admin.site.index_title = 'Margy Site Administration'
