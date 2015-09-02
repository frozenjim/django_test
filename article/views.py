from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from django.template.loader import get_template
from django.views.generic import TemplateView

from article.models import Article


def articles(request):
    """
    I updated render_to_request to "render" because
    render_to_request will be deprecated in v2.0
    according to the devs.
    """

    language = 'en-us'
    session_language = 'en-us'

    if 'lang' in request.COOKIES:
        language = request.COOKIES['lang']

    if 'lang' in request.session:
        session_language = request.session['lang']

    return render(
        request,
        'articles.html',
        {'articles': Article.objects.all(),
            'language': language,
            'session_language': session_language,
         }
    )


def article(request, article_id=1):
    return render(
        request,
        'article.html',
        {'article': Article.objects.get(id=article_id)}
    )


def language(request, language='en-us'):
    response = HttpResponse("setting language to %s" % language)

    response.set_cookie('lang', language)

    request.session['lang'] = language
    return response


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
