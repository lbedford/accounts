from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django import forms

from accounts.models import LbwUser

class UserCreateForm(UserCreationForm):
  profile_image = forms.ImageField(required=False)

  class Meta:
    model = User
    fields = ("username", "email", "first_name", "last_name", "profile_image")

class UserUpdateForm(UserChangeForm):
  profile_image = forms.ImageField(required=False)

  class Meta:
    model = User
    fields = ( "username", "email", "first_name", "last_name", "profile_image")

  def clean_password(self):
    # is this a bug?
    return ""

class LbwUserForm(forms.ModelForm):
  class Meta:
    model = LbwUser

class LoginForm(forms.Form):
  username = forms.CharField()
  password = forms.CharField(widget=forms.PasswordInput())
