"""Views for the accounts application."""

import urllib

from accounts.forms import UserCreateForm
from accounts.forms import UserUpdateForm
from accounts.forms import LoginForm
from accounts.models import LbwUser
from django.contrib import auth
from django.contrib.auth.models import User
from django.core.mail import mail_admins
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.shortcuts import redirect

def index(request):
  """Index view."""
  return render(request, 'accounts/index.html')

def register(request):
  """Register user view. Render a blank form, or validate a post."""
  if request.method == 'POST':
    form = UserCreateForm(request.POST)
    if form.is_valid():
      user = form.save()
      user.is_active = False
      user.save()
      lbwuser = LbwUser(user=user)
      lbwuser.save()
      message = """A new user:
%s %s
has signed up. Please check
http://%s%s
and activate them as necessary.
"""
      mail_admins("New User registered",
                  message % (user.get_full_name(), user.email, request.get_host(), reverse('activate_users')))
      return redirect('index')
  else:
    form = UserCreateForm()
  return render(request, 'accounts/create_user.html',
      {'form': form})

def profile(request):
  """Show user profile, allow them to update it."""
  if not request.user.is_authenticated():
    return HttpResponseRedirect(reverse('index'))
  if request.method == 'POST':
    form = UserUpdateForm(request.POST or None, instance=request.user)
    if form.is_valid():
      form.save()
      if 'profile_image' in request.FILES:
        try:
          lbwuser = request.user.lbwuser
          lbwuser.profile_image = request.FILES['profile_image']
          lbwuser.save()
        except LbwUser.DoesNotExist:
          lbwuser = LbwUser(user=request.user,
                            profile_image=request.FILES['profile_image'])
          lbwuser.save()
      return redirect('index')
  else:
    try:
      lbwuser = request.user.lbwuser
    except LbwUser.DoesNotExist:
      lbwuser = LbwUser(user=request.user)
      lbwuser.save()
    form = UserUpdateForm(instance=request.user)
  return render(request, 'accounts/profile.html',
      {'form': form})

def login(request):
  """Login. Looks up by username or email address."""
  if request.user.is_authenticated():
    return HttpResponseRedirect(reverse('index'))
  if request.method == 'POST':
    form = LoginForm(request.POST)
    if form.is_valid():
      user = auth.authenticate(username=request.POST['username'],
                               password=request.POST['password'])
      if not user:
        try:
          email_user = User.objects.get(
              email__exact=request.POST['username'])
          user = auth.authenticate(username=email_user.username,
                                   password=request.POST['password'])
        except User.DoesNotExist:
          user = None
      if user:
        if user.is_active:
          auth.login(request, user)
          if 'next' in request.POST:
            return HttpResponseRedirect(request.POST['next'])
          else:
            return HttpResponseRedirect(reverse('index'))
        else:
          form.errors['username'] = 'This user is not active yet, please try later.'
      else:
        form.errors['username'] = (
            'username or email address not found and/or password wrong')
  else:
    form = LoginForm()
    next_url = urllib.unquote_plus(request.GET.get('next', '')).decode('utf8')
  return render(request, 'accounts/login.html', {'login_form': form,
                                                 'next': next_url})

def activate_users(request):
  """Print a list of users who need to be activated."""
  if request.user.is_superuser:
    users = User.objects.filter(is_active__exact=False)
    return render(request, 'accounts/activate_users.html', {'users': users})
  else:
    return HttpResponseRedirect(reverse('index'))

def activate_user(request, user_id):
  """Activate a user."""
  if request.user.is_superuser:
    user = get_object_or_404(User, pk=user_id)
    user.is_active = True
    user.save()
    try:
      unused_lbwuser = user.lbwuser
    except LbwUser.DoesNotExist:
      lbwuser = LbwUser(user=user)
      lbwuser.save()
    user.email_user("Account activated",
                    "Your LBW account has been activated.\n"
                    "Please visit %s to login." % request.build_absolute_uri(reverse('login')))
    return HttpResponseRedirect(reverse('activate_users'))
  else:
    return HttpResponseRedirect(reverse('index'))
