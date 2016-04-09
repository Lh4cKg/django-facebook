# -*- coding: utf-8 -*-

from django.conf.urls import url, patterns
from facebook import views

urlpatterns = [
		url(r'^$', views.home, name='home'),
		url(r'^facebook/$', views.facebook_login, name='login'),
		url(r'^callback/$', views.callback, name='callback'),
]