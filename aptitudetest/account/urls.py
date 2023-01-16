from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('login/', name='login'),
    path('logout/', name='logout'),
    path('password_change/', name='password_change'),
    path('password_change/done/', name='password_change_done'),
    path('password_reset/', name='password_reset'),
    path('password_reset/done/', name='password_reset_done'),
    path('reset/<uidb64>/<token>/', name='password_reset_confirm'),
    path('reset/done/', name='password_reset_complete')
]