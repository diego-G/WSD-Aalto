from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, RequestContext
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.contrib.auth import *
from django.http import Http404

from django.core.context_processors import csrf

def home(request):
    
    c = {}
    c.update(csrf(request))
    if not request.user.is_authenticated():
        return render_to_response('index.html',c, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect("/" + request.user.username + "/")
    
def login_error(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('index.html',c, context_instance=RequestContext(request))