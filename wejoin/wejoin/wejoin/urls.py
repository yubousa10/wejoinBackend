"""wejoin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns

from register import api

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),# admin logn in
    url(r'^api/authToken/$', api.doAuth.as_view()),# atuh for you
    url(r'^api/getToken/$', api.TokenForUser.as_view()),# get token for specific email
    url(r'^api/userlist/$', api.UserList.as_view()), # get all user info or post an user
    url(r'^api/getUserByemail/$', api.getUserbyEmail.as_view()),# get user by email
    
    url(r'^api/getRegisterInfoByemail/$', api.getRegisterInfoByemail.as_view()),# get an user register info by email
    url(r'^api/RegisterinfoList/$', api.RegisterList.as_view())# get all register info or post register info for specific user by user id
]
