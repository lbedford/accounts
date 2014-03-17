from accounts.forms import UserCreateForm
from accounts.forms import UserUpdateForm
from django.shortcuts import render
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

def register(request):
  if request.method == 'POST':
    form = UserCreateForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('registration:index')
  else:
    form = UserCreateForm()
  return render(request, 'accounts/create_user.html',
      {'form': form})

def update_user(request):
  form = UserUpdateForm(instance=request.user)
  return render(request, 'accounts/update_user.html',
      {'form': form})

def profile(request):
  if not request.user.is_authenticated():
    return redirect(reverse('django.contrib.auth.views.login'))
  return render(request, 'accounts/profile.html')
