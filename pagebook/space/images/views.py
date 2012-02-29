from django.template import Context, RequestContext
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.contrib.auth import *
from django.http import Http404
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.http import (HttpResponse, HttpResponseRedirect,
                          HttpResponseBadRequest)
from form import ImageUploadForm

from settings import MEDIA_ROOT

def images(request, name):
    template = "space/images/images.html"
    
    c = {}
    c.update(csrf(request))
    try:
        usr = User.objects.get(username=name)
    except usr.DoesNotExist:
        raise Http404
    
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        save_file(request.FILES['image'])
        return HttpResponseRedirect(".")

    else:
        if request.user.is_authenticated():
            if request.user==usr:  
                form = ImageUploadForm()          
                return render_to_response(template, RequestContext(request,{
                    'user':request.user, 'owner':usr, 'form': form,  'images': MEDIA_ROOT+"/images/"
                }))
            else:
                raise Http404
        else:
            raise Http404

def save_file(file, path=''):
    filename = file._get_name()
    fd = open('%s/%s' % (MEDIA_ROOT+"/images/", str(path) + str(filename)), 'wb')
    for chunk in file.chunks():
        fd.write(chunk)
    fd.close()