
from django.conf.urls import patterns, include, url

urlpatterns = [
    url(r'^profile/$', views.index, name='index'),
]