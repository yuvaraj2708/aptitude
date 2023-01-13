from django.forms import ModelForm
from django import forms
from .models import *
    
    
class TestForm(ModelForm):
        class Meta:
            model = Department,Role,Topic
            fields = '__all__'