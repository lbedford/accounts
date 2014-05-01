from django.conf.urls import patterns, url
from accounts import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^activate_users/$', views.activate_users, name='activate_users'),
    url(r'^activate_user/(?P<user_id>\d+)$', views.activate_user, name='activate_user'),

    url(r'^changepassword/$', 'django.contrib.auth.views.password_change',
        kwargs={'template_name': 'accounts/password_change_form.html'}),
    url(r'^change_password_done/$',
        'django.contrib.auth.views.password_change_done',
        kwargs={'template_name': 'accounts/password_change_done.html'},
        name='password_change_done'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        kwargs={'template_name': 'accounts/logged_out.html'}),
    url(r'^resetpassword/$', 'django.contrib.auth.views.password_reset',
        kwargs={'template_name': 'accounts/password_reset_form.html',
                'email_template_name': 'accounts/password_reset_email.html'}),
    url(r'^reset_password_confirm/(?P<uidb36>[^/]+)/(?P<token>.+)$',
        'django.contrib.auth.views.password_reset_confirm',
        kwargs={'template_name': 'accounts/password_reset_confirm.html'}),
    url(r'^reset_password_done/$',
        'django.contrib.auth.views.password_reset_done',
        kwargs={'template_name': 'accounts/password_reset_done.html'}),
    url(r'^reset_password_complete/$',
        'django.contrib.auth.views.password_reset_complete',
        kwargs={'template_name': 'accounts/password_reset_complete.html'}),
)
