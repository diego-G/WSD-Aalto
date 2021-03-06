from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, RequestContext
from django.core.context_processors import csrf
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.contrib.auth import *
from django.http import Http404
from django.conf import settings

from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.core.context_processors import csrf
import os
from settings import MEDIA_ROOT

FACEBOOK_APP_ID = getattr(settings, 'FACEBOOK_APP_ID', '')
FACEBOOK_API_KEY = getattr(settings, 'FACEBOOK_API_KEY', '')
FACEBOOK_SECRET_KEY = getattr(settings, 'FACEBOOK_SECRET_KEY', '')

def login_view(request):
    """
    After receive the login and password, It is checked the existence of the user and the correct pass
    """ 
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
            return HttpResponseRedirect("/login_error/")
    else:
        return HttpResponse("no post")

def logout_view(request):
    """
    Redirecting to the fron-page when logout from anywhere
    """ 
    logout(request)
    return HttpResponseRedirect("/")

def register(request):
    """
    Showing the registration form and creating the new user.
    It creates a folder for each new user to hold their images.
    """ 
    form = UserCreationForm()
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
