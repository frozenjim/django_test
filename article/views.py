from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.views.generic import TemplateView

from article.models import Article


def articles(request):
    return render_to_response(
        'articles.html',
        {'articles': Article.objects.all()})


def article(request, article_id=1):
    return render_to_response(
        'article.html',
        {'article': Article.objects.get(id=article_id)}
    )


def hello(request):
    name = "James"
    html = "<html><body>Hi %s, this seems to have worked!</body></html>" % name
    return HttpResponse(html)


def hello_template(request):
    name = "James"
    t = get_template('hello.html')
    html = t.render({'name': name}, request)
    return HttpResponse(html)


def hello_template_simple(request):
    name = "James"
    return render_to_response('hello.html', {'name': name})


class HelloTemplate(TemplateView):

    template_name = 'hello_class.html'

    def get_context_data(self, **kwargs):
        context = super(HelloTemplate, self).get_context_data(**kwargs)
        context['name'] = 'James'
        return context
