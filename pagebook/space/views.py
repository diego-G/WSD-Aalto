from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.contrib.auth import *
from django.http import Http404


def home(request, name):

    if not request.user.is_authenticated():
        return HttpResponse("only see")
    else:
        return render_to_response("about.html", Context({'user':name}))