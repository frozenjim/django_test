# django.CORE.context_processors is deprecated.
# use django.TEMPLATE.context_processors instead
from django.template.context_processors import csrf

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import get_template
from django.views.generic import TemplateView

from article.models import Article
from .forms import ArticleForm


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


def create(request):
    if request.POST:
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/articles/all')
    else:
        form = ArticleForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render(
        request,
        'create_article.html',
        args
    )


def like_article(request, article_id):
    if article_id:
        a = Article.objects.get(id=article_id)
        count = a.likes
        count += 1
        a.likes = count
        a.save()

    return HttpResponseRedirect('/articles/get/%s' % article_id)


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
    return render(request, 'hello.html', {'name': name})


class HelloTemplate(TemplateView):

    template_name = 'hello_class.html'

    def get_context_data(self, **kwargs):
        context = super(HelloTemplate, self).get_context_data(**kwargs)
        context['name'] = 'James'
        return context
