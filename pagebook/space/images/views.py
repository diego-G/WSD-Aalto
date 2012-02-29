from django.template import Context, RequestContext
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.contrib.auth import *
from django.http import Http404
from django.contrib.auth.models import User
from django.core.context_processors import csrf
from django.http import (HttpResponse, HttpResponseRedirect,
                          HttpResponseBadRequest)

from settings import MEDIA_ROOT

def images(request, name):
    template = "space/images/images.html"
    c = {}
    c.update(csrf(request))
    try:
        usr = User.objects.get(username=name)
    except usr.DoesNotExist:
        raise Http404
    if request.user.is_authenticated():
        if request.user==usr:            
            return render_to_response(template, RequestContext(request,{
                'user':request.user, 'owner':usr,
            }))
        else:
            raise Http404
    else:
        raise Http404
 
    if request['method'] == 'POST':
        if 'file' in request.FILES:
            file = request.FILES['file']
 
            filename = file['filename']
 
            fd = open('%s/%s' % (MEDIA_ROOT, filename), 'wb')
            fd.write(file['content'])
            fd.close()
 
            return http.HttpResponseRedirect(template)
    else:
        # display the form
        form = ImageUploadForm()
        return render_to_response(template, { 'form': form })