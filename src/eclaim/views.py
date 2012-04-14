'''
Created on Mar 6, 2012

@author: Sun_2
'''
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response

@login_required
def index(request):
    return render_to_response('index.html',
                               context_instance=RequestContext(request),
                               )