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
from django.conf.urls import url, patterns, include
from django.contrib.auth.models import User, Group
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from register import api
admin.autodiscover()
from rest_framework import permissions, routers, serializers, viewsets
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, TokenHasScope


# first we define the serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['groups']
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


# Routers provide an easy way of automatically determining the URL conf
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),# admin logn in
                       
    url(r'^', include(router.urls)),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    
    
    url(r'^api/userlist/$', api.UserList.as_view()), # get all user info or post an user
    url(r'^api/getUserByemail/$', api.getUserbyEmail.as_view()),# get user by email
    
    url(r'^api/getRegisterInfoByemail/$', api.getRegisterInfoByemail.as_view()),# get an user register info by email
    url(r'^api/RegisterinfoList/$', api.RegisterList.as_view())# get all register info or post register info for specific user by user id
)
