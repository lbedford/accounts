from accounts.forms import UserCreateForm
from accounts.forms import UserUpdateForm
from accounts.forms import LoginForm
from accounts.models import LbwUser
from django.contrib import auth
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect

def index(request):
  return render(request, 'accounts/index.html')

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

def profile(request):
  if not request.user.is_authenticated():
    return redirect('django.contrib.auth.views.login')
  if request.method == 'POST':
    form = UserUpdateForm(request.POST or None, instance=request.user)
    if form.is_valid():
      form.save()
      if 'profile_image' in request.FILES:
        try:
          lbwuser = LbwUser.objects.get(user_id__exact=request.user.id)
          lbwuser.profile_image = request.FILES['profile_image']
          lbwuser.save()
        except LbwUser.DoesNotExist:
          lbwuser.create(user=user, profile_image=request.FILES['profile_image'])
          lbwuser.save()
      return redirect('registration:index')
  else:
    form = UserUpdateForm(instance=request.user)
  return render(request, 'accounts/profile.html', 
      {'form': form})

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

def activate_users(request):
  if request.user.is_superuser:
    try:
      users = User.objects.get(is_active__exact=False)
    except User.DoesNotExist:
      users = []
    return render(request, 'accounts/activate_users.html', {'users': users})
  else:
    redirect('index')
