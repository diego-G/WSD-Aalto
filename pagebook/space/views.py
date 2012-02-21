from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, RequestContext
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.contrib.auth import *
from django.http import Http404
from django.contrib.auth.models import User
from models import Album, Page, Image, AlbumForm
from django.core.context_processors import csrf

def home(request, name):

    if not request.user.is_authenticated():
        return render_to_response("space/album.html", {})
    else:
        usr = User.objects.get(username=name)
        albums = Album.objects.filter(user=usr)
        if not albums:
            return HttpResponseRedirect("create_album/")
        
        return render_to_response("space/album.html", Context({'user':name, 'albums':albums}))


def create(request, name):
    c = {}
    c.update(csrf(request))
    if request.method == 'POST': # If the form has been submitted...
        usr = User.objects.get(username=name)
        album = Album(user=usr)
        form = AlbumForm(request.POST, instance=album) # A form bound to the POST data
        form.save()
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            return HttpResponseRedirect('/') # Redirect after POST
    else:
        form = AlbumForm() # An unbound form

    return render_to_response('space/create_album.html', RequestContext(request,{
        'form': form,
    }))

def delete(request, name, album):
#def delete(request, name):
    #faltan los try
    usr = User.objects.get(username=request.user.username)
#    Album.objects.get(user=usr, name=album).delete()
    Album.objects.filter(user=usr, id=album).delete()
    return HttpResponseRedirect("/")