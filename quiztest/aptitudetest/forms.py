from django.forms import ModelForm
from .models import *
    
    
class TestForm(ModelForm):
    class Meta:
        model = Department,Role,Topic
        fields = '__all__'

