"""Urls for acccounts app."""
from django.urls import path
from django.contrib.auth import views as django_views

from accounts import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('profile', views.profile, name='profile'),
    path('activate_users', views.activate_users, name='activate_users'),
    path('activate_user/<int:user_id>',
         views.activate_user, name='activate_user'),

    path('logout/',
         django_views.LogoutView.as_view(next_page='registration:index',
                                         template_name='accounts/logged_out.html'),
         name='logout'),

    path('password_change',
         django_views.PasswordChangeView.as_view(
             template_name='accounts/password_change_form.html'),
         name='password_change'),
    path('password_change/done',
         django_views.PasswordChangeDoneView.as_view(
             template_name='accounts/password_change_done.html'),
         name='password_change_done'),
    path('password_reset',
         django_views.PasswordResetView.as_view(
             template_name='accounts/password_reset_form.html',
             email_template_name='accounts/password_reset_email.html'),
         name='password_reset'),
    path('password_reset/done',
         django_views.PasswordResetDoneView.as_view(
             template_name='accounts/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         django_views.PasswordResetConfirmView.as_view(
             template_name='accounts/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('reset/done',
         django_views.PasswordResetCompleteView.as_view(
             template_name='accounts/password_reset_complete.html'),
         name='password_reset_complete'),
]
