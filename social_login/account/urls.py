from django.urls import path,re_path
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from django.contrib.auth.views import logout_then_login
from django.contrib.auth.views import password_change
from django.contrib.auth.views import password_change_done
from django.contrib.auth.views import password_reset
from django.contrib.auth.views import password_reset_complete
from django.contrib.auth.views import password_reset_confirm
from django.contrib.auth.views import password_reset_done
from account import views

urlpatterns = [
	re_path(r'^$', views.dashboard, name='dashboard'),
    re_path(r'^register/$', views.register, name='register'),

    # login logout
    re_path(r'^login/$', login, name='login'),
    re_path(r'^logout/$', logout, name='logout'),
    re_path(r'^logout-then-login/$', logout_then_login, name='logout_then_login'),

    # change password
    re_path(r'^password-change/$', password_change, name='password_change'),
    re_path(r'^password-change/done/$', password_change_done, name='password_change_done'),

    # reset password
    # restore password re_paths
    re_path(r'^password-reset/$',
        password_reset,
        name='password_reset'),
    re_path(r'^password-reset/done/$',
        password_reset_done,
        name='password_reset_done'),
    re_path(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
        password_reset_confirm,
        name='password_reset_confirm'),
    re_path(r'^password-reset/complete/$',
        password_reset_complete,
        name='password_reset_complete'),
]