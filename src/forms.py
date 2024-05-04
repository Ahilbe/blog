from django import forms
from .models import Store
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignInForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class BlogForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ('__all__')
