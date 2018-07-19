"""newsadm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
	1. Add an import:  from my_app import views
	2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
	1. Add an import:  from other_app.views import Home
	2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
	1. Import the include() function: from django.conf.urls import url, include
	2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from newsadmapp import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^index/$', views.index),
	url(r'^index/(\d+)/$', views.index),
	url(r'^detail/(\d+)/$', views.detail),
	url(r'^login/$', views.login),
	url(r'^logout/$', views.logout),
	url(r'^adminmain/$', views.adminmain),
	url(r'^adminmain/(\d+)/$', views.adminmain),
 	url(r'^newsadd/$', views.newsadd),
	url(r'^newsedit/(\d+)/$', views.newsedit),
	url(r'^newsedit/(\d+)/(\d+)/$', views.newsedit),
	url(r'^newsdelete/(\d+)/$', views.newsdelete),
	url(r'^newsdelete/(\d+)/(\d+)/$', views.newsdelete),
	url(r'^admin/', admin.site.urls),
]
