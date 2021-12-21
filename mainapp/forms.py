from django import forms
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        # Making location required
        self.fields['email'].required = True
        self.fields['is_superuser'].required = True
        self.fields['is_staff'].required = True

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'is_staff', 'is_superuser']
        

