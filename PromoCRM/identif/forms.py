from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    class Meta():
        model = User
        fields = ['username','last_name', 'first_name','email', 'password1', 'password2']