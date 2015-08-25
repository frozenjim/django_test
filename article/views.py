from django.http import HttpResponse
# from django.shortcuts import render


def hello(request):
    name = "James"
    html = "<html><body>Hi %s, this seems to have worked!</body></html>" % name
    return HttpResponse(html)
