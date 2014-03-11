from accounts.forms import UserCreateForm
from django.shortcuts import render
from django.contrib.auth.models import User

def register(request):
  if request.method == 'POST':
    form = UserCreateForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('registration:index')
  else:
    form = UserCreateForm()
  return render(request, 'registration/create_user.html',
      {'form': form})
