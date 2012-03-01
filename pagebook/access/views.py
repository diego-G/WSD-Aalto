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

import os
from settings import MEDIA_ROOT

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
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():          
            new_user = form.save()
            
            #It creates a private folder for each user 
            os.mkdir(os.path.join(MEDIA_ROOT+"/images/", new_user.username))
            
            return HttpResponseRedirect("/")
    else:
        form = UserCreationForm()

    return render_to_response("access/register.html", {
        'form' : form} , context_instance=RequestContext(request) 
    )