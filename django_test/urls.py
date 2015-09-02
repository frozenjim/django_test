"""djtest URL Configuration

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

from article.views import HelloTemplate


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    # User auth urls
    url(r'^accounts/login/$', 'django_test.views.login'),
    url(r'^accounts/auth/$', 'django_test.views.auth_view'),
    url(r'^accounts/logout/$', 'django_test.views.logout'),
    url(r'^accounts/loggedin/$', 'django_test.views.loggedin'),
    url(r'^accounts/invalid/$', 'django_test.views.invalid_login'),

    # From previous tutorials
    url(r'^$', 'django_test.views.home', name='home'),
    url(r'^hello/$', 'article.views.hello', name='fake_hello'),
    url(r'^hello_template/$', 'article.views.hello_template', name='hello_template'),
    url(r'^hello_template_simple/$', 'article.views.hello_template_simple', name='hello_template_simple' ),
    url(r'^hello_class_view/$', HelloTemplate.as_view(), name='hello_class_view'),
    url(r'^articles/', include('article.urls', namespace='articles')),
]
