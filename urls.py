from django.conf.urls import url
from accounts import views
from django.contrib.auth import views as django_views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^activate_users/$', views.activate_users, name='activate_users'),
    url(r'^activate_user/(?P<user_id>\d+)$', views.activate_user, name='activate_user'),

    # copied from contrib/auth/urls.py
    url(r'^logout/$', django_views.logout, name='logout',
        kwargs={'template_name': 'accounts/logged_out.html'}),
    url(r'^password_change/$', django_views.password_change,
        name='password_change',
        kwargs={'template_name': 'accounts/password_change_form.html'}),
    url(r'^password_change/done/$', django_views.password_change_done,
        name='password_change_done',
        kwargs={'template_name': 'accounts/password_change_done.html'}),
    url(r'^password_reset/$', django_views.password_reset,
        name='password_reset',
        kwargs={'template_name': 'accounts/password_reset_form.html',
                'email_template_name': 'accounts/password_reset_email.html'}),
    url(r'^password_reset/done/$', django_views.password_reset_done,
        name='password_reset_done',
        kwargs={'template_name': 'accounts/password_reset_done.html'}),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        django_views.password_reset_confirm, name='password_reset_confirm',
        kwargs={'template_name': 'accounts/password_reset_confirm.html'}),
    url(r'^reset/done/$', django_views.password_reset_complete,
        name='password_reset_complete',
        kwargs={'template_name': 'accounts/password_reset_complete.html'}),
]
