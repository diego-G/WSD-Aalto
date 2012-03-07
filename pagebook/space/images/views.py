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

from django.contrib.auth.decorators import login_required
from settings import MEDIA_URL,MEDIA_ROOT
import os

@login_required
def images(request, name):
    template = "space/images/images.html"
    
    c = {}
    c.update(csrf(request))
    try:
        usr = User.objects.get(username=name)
    except User.DoesNotExist:
        raise Http404
    
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)  
        save_file(request.FILES['image'],usr)
        return HttpResponseRedirect(".")

    else:
        if request.user==usr:  
            form = ImageUploadForm()
            try:
                os.mkdir(os.path.join(MEDIA_ROOT+"/images/", usr.username))
            except OSError:
                pass
            path = MEDIA_ROOT+"/images/"+usr.username
            listing = os.listdir(path)
            return render_to_response(template, RequestContext(request,{
                'user':request.user, 'owner':usr, 'form': form, 'listing': listing
            }))
        else:
            raise Http404

def save_file(file, user, path=''):
    filename = file._get_name()
    fd = open('%s/%s' % (MEDIA_ROOT+"/images/"+user.username, str(path) + str(filename)), 'wb')
    for chunk in file.chunks():
        fd.write(chunk)
    fd.close()
    
def delete_image(request, name, file):
    os.remove(MEDIA_ROOT+"/images/"+name+"/"+file)
    return HttpResponseRedirect("../")