'''
Created on Mar 6, 2012

@author: Sun_2
'''
from django.http import HttpResponse
from django.template import Context, loader

def index(request):
    indexTemplate = loader.get_template("index.html");
    context = Context({});
    return HttpResponse(indexTemplate.render(context));
