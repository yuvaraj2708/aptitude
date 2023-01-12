
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

