"""Forms for accounts app."""
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django import forms

# pylint: disable=W0232
# pylint: disable=C1001
# pylint: disable=R0903

class UserCreateForm(UserCreationForm):
  """Form to create a user."""
  profile_image = forms.ImageField(required=False)

  class Meta(object):
    """Meta."""
    model = User
    fields = ("username", "email", "first_name", "last_name", "profile_image")

class UserUpdateForm(UserChangeForm):
  """Form to update a user record."""
  profile_image = forms.ImageField(required=False)

  class Meta(object):
    """Meta."""
    model = User
    fields = ("username", "email", "first_name", "last_name", "profile_image")

  def clean_password(self):
    # is this a bug?
    return ""

class LoginForm(forms.Form):
  """Basic form for login."""
  username = forms.CharField()
  password = forms.CharField(widget=forms.PasswordInput())
