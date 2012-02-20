from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.contrib.auth import *
from django.http import Http404

from django.core.context_processors import csrf

def home(request):
    
    c = {}
    c.update(csrf(request))
    
    return render_to_response('index.html', c)