
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.http import Http404

def home(request):
    return render_to_response('index.html',{})