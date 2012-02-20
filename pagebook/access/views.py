from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context
from django.core.context_processors import csrf
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.contrib.auth import *
from django.http import Http404

from django.core.context_processors import csrf


def login_view(request):
    
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect("/" + username + "/")
            else:
                return HttpResponse("not active")
        else:
            return HttpResponse("bad password")
    else:
        return HttpResponse("no post")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")