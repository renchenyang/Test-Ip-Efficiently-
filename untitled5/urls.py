"""untitled5 URL Configuration

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

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'default.views.getlist'),
    url(r'^todogetlist/$', "default.views.todogetlist"),
    url(r'^update/$', 'default.views.updatelist'),
    url(r'^del/$', 'default.views.dellist'),
    url(r'^add/$', 'default.views.addlist'),
    url(r'^add2/$', 'default.views.addlist2'),
    url(r'^history/$', 'default.views.history'),
    url(r'^account/login/$', 'default.views.login2'),
    url(r'^account/logout/$', 'default.views.logout_view'),
    url(r'^getlist2/todogetlist/$', "default.views.todogetlist"),
    url(r'^getlist2/$', 'default.views.getlist2'),
    url(r'^refresh/$', 'default.views.refresh'),
]
