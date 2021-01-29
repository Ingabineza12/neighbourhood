from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *


class UserRegisterForm(UserCreationForm):
   email = forms.EmailField(max_length=200, help_text = 'Required')
   class Meta:
       model = User
       fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image','bio']

class NeighbourhoodForm(forms.ModelForm):
    class Meta:
        model=Neighbourhood
        fields = ['name','location','population','image']

class NewBusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields=['name','description','email']
class NewPostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['post']
