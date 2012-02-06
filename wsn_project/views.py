
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.http import Http404

def home(request):
    return render_to_response('index.html',{})

def auth(request):
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect("/account/user/")
            else:
                return HttpResponse("not active")
        else:
            return HttpResponse("user None")
    else:
        return HttpResponse("no post")

