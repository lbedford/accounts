from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django import forms

from accounts.models import LbwUser

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)
    firstname = forms.CharField(required=True)
    lastname = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ( "username", "email", "firstname", "lastname")

class UserUpdateForm(UserChangeForm):
  class Meta:
    model = User
    fields = ( "username", "email", "first_name", "last_name")

class LbwUserForm(forms.ModelForm):
  class Meta:
    model = LbwUser

class LoginForm(forms.Form):
  username = forms.CharField()
  password = forms.CharField(widget=forms.PasswordInput())
