from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.hello, name='hello'),
    url(r'^all/$', views.articles, name='articles'),
    url(r'get/(?P<article_id>[0-9+])', views.article, name='get_article'),
    url(r'^language/(?P<language>[a-z\-]+)/$', 'article.views.language', name='set_language'),
]
