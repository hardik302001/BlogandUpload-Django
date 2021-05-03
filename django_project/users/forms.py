#This file takes in extra field for forms
#because in default form we did not have email
#it only had username, password and again verify password

from django import forms

from django.contrib.auth.models import User   #import the actual user form that will inherit it
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


#new form that inherits from the User form
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:    #keep final configurations
        model = User   #we want this form to interact with this model
        fields  = ['username','email','password1','password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:  # keep final configurations
        model = User  # we want this form to interact with this model
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']