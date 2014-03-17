from accounts.forms import UserCreateForm
from accounts.forms import UserUpdateForm
from accounts.forms import LoginForm
from django.contrib import auth
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect

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

def login(request):
  if request.method == 'POST':
    form = LoginForm(request.POST)
    if form.is_valid():
      user = auth.authenticate(username=request.POST['username'],
                               password=request.POST['password'])
      if not user:
        print 'Failed to login as username, trying an email'
        try:
          email_user = User.objects.get(
              email__exact=request.POST['username'])
          user = auth.authenticate(username=email_user.username,
                                   password=request.POST['password'])
        except Exception, e:
          print e
      if user:
        if user.is_active:
          auth.login(request, user)
          if 'next' in request.POST:
            return HttpResponseRedirect(request.POST['next'])
          else:
            return HttpResponseRedirect(reverse('registration:index'))
        else:
          form.errors['username'] = 'This user is not active'
      else:
        form.errors['username'] = 'Invalid username and/or password'
  else:
    form = LoginForm()
  return render(request, 'accounts/login.html', {'login_form': form})
