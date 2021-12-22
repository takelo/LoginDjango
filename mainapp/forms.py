from django import forms
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):

    

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        # Making location required
        self.fields['email'].required = True
        # self.fields['is_superuser'].required = True
        # self.fields['is_staff'].value = True

    class Meta:
        model = User
        # model.is_staff = True
        # fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'is_staff', 'is_superuser']
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

    def save(self, commit=True):
        user = super (RegisterForm , self ).save(commit=False)
        user.username = self.cleaned_data ['username']
        user.email = self.cleaned_data ['email']
        user.first_name = self.cleaned_data ['first_name']
        user.last_name = self.cleaned_data ['last_name']
        user.password1 = self.cleaned_data ['password1']
        user.password2 = self.cleaned_data ['password2']
        user.is_staff = True
        user.is_superuser = True

        if commit :
            user.save()

        return user
        



  

