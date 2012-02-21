from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, RequestContext
from django.core.context_processors import csrf
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.contrib.auth import *
from django.http import Http404

from django import forms
from django.contrib.auth.forms import UserCreationForm

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

def register(request):
    
    form = UserCreationForm()

    if request.method == 'POST':
        data = request.POST.copy()
        errors = form.get_validation_errors(data)
        if not errors:
            new_user = form.save(data)
            return HttpResponseRedirect("/" + username + "/")
    else:
        data, errors = {}, {}

    return render_to_response("access/register.html", {
        'form' : form }, context_instance=RequestContext(request)
    )