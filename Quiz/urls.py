from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.log,name="Home"),
    path("register/",views.reg,name="registerpage"),
    path("depart/",views.department,name="departmentpage"),
    path("test/",views.Test,name="testpage"),

    path('add/', views.person_create_view, name='person_add'),
    path('<int:pk>/', views.person_update_view, name='person_change'),
    path('ajax/load-roles/', views.load_cities, name='ajax_load_roles'), # AJAX
]

admin.site.index_title = 'Margy Site Administration'
