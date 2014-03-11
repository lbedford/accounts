from django.conf.urls import patterns, url
from django.contrib.auth.views import password_change
from django.contrib.auth.views import password_change_done
from django.contrib.auth.views import password_reset
from django.contrib.auth.views import password_reset_done
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from accounts import views

urlpatterns = patterns('',
#    url(r'^$', views.index),
    url(r'^changepassword/$', 'django.contrib.auth.views.password_change'),
    url(r'^change_password_done/$',
        'django.contrib.auth.views.password_change_done'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^resetpassword/$', 'django.contrib.auth.views.password_reset'),
    url(r'^reset_password_done/$',
        'django.contrib.auth.views.password_reset_done'),
    url(r'^register/$', views.register, name='register'),
)
