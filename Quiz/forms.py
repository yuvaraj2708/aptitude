
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from Quiz.models import Person, Role
# class UserRegistrationForm(forms.Form):
#     username = forms.CharField(
#         required = True,
#         label = 'Username',
#         max_length = 32
#     )
#     email = forms.CharField(
#         required = True,
#         label = 'Email',
#         max_length = 32,
#     )
#     password = forms.CharField(
#         required = True,
#         label = 'Password',
#         max_length = 32,
#         widget = forms.PasswordInput()
#     )


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

def create_superuser(self, email, username, password):

         user = self.create_user(
            email,
            username,
            password=password,
        )
         user.is_admin = True
         user.save(using=self._db)
         return user

#Samples

class PersonCreationForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['role'].queryset = Role.objects.none()
    

        if 'Department' in self.data:
            try:
                Department_id = int(self.data.get('Department'))
                self.fields['role'].queryset = Role.objects.filter(Department_id=Department_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
             self.fields['role'].queryset = self.instance.Department.role_set.order_by('name')
            