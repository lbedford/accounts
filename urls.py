from django.conf.urls import patterns, url
from django.contrib.auth.views import password_change
from django.contrib.auth.views import password_change_done
from django.contrib.auth.views import password_reset
from django.contrib.auth.views import password_reset_confirm
from django.contrib.auth.views import password_reset_complete
from django.contrib.auth.views import password_reset_done
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from accounts import views

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^changepassword/$', 'django.contrib.auth.views.password_change',
        kwargs={'template_name': 'accounts/password_change_form.html'}),
    url(r'^change_password_done/$',
        'django.contrib.auth.views.password_change_done',
        kwargs={'template_name': 'accounts/password_change_done.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        kwargs={'template_name': 'accounts/logged_out.html'}),
    url(r'^login/$', views.login, name='login'),
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
    url(r'^register/$', views.register, name='register'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^activate_users/$', views.activate_users, name='activate_users'),
)
