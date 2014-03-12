from accounts.forms import UserCreateForm
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

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
  form = UserChangeForm(instance=request.user)
  return render(request, 'accounts/update_user.html',
      {'form': form})
