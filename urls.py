from django.urls import path
from accounts import views
from django.contrib.auth import views as django_views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('profile', views.profile, name='profile'),
    path('activate_users', views.activate_users, name='activate_users'),
    path('activate_user/<int:user_id>', views.activate_user, name='activate_user'),

    path('logout/', django_views.LogoutView.as_view(), name='logout',
        kwargs={'template_name': 'accounts/logged_out.html'}),
    path('password_change', django_views.PasswordChangeView.as_view(),
        name='password_change',
        kwargs={'template_name': 'accounts/password_change_form.html'}),
    path('password_change/done', django_views.PasswordChangeDoneView.as_view(),
        name='password_change_done',
        kwargs={'template_name': 'accounts/password_change_done.html'}),
    path('password_reset', django_views.PasswordResetView.as_view(),
        name='password_reset',
        kwargs={'template_name': 'accounts/password_reset_form.html',
                'email_template_name': 'accounts/password_reset_email.html'}),
    path('password_reset/done', django_views.PasswordResetDoneView.as_view(),
        name='password_reset_done',
        kwargs={'template_name': 'accounts/password_reset_done.html'}),
    path('reset/<uidb64>/<token>/', django_views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm',
        kwargs={'template_name': 'accounts/password_reset_confirm.html'}),
    path('reset/done', django_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete',
        kwargs={'template_name': 'accounts/password_reset_complete.html'}),
]
