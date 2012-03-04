from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from space.models import Album, Page, Image, AlbumForm, PageForm
from django.core.context_processors import csrf

from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.shortcuts import render_to_response
from django.template import Context, RequestContext

from settings import MEDIA_ROOT
import os

@login_required
def edit_page(request, name, album, page ):
    try:
        usr = User.objects.get(username=name)
    except User.DoesNotExist:
        raise Http404
    try:
        album_ = Album.objects.get(user=usr, id=album)
    except Album.DoesNotExist:
        raise Http404
    page_ = Page.objects.get(album=album_, number=page)
    
    path = MEDIA_ROOT+"/images/"+usr.username
    try:
        listing = os.listdir(path)
    except OSError:
        listing = ''
    
    return render_to_response("space/editor/edit_page.html", RequestContext(request,{
              'user':request.user, 'album': album_, 'page':page_, 'listing': listing
    }))
    
def choose_image(request, name, album, page ):
    try:
        usr = User.objects.get(username=name)
    except User.DoesNotExist:
        raise Http404
    try:
        album_ = Album.objects.get(user=usr, id=album)
    except Album.DoesNotExist:
        raise Http404
    page_ = Page.objects.filter(album=album_)
    
    path = MEDIA_ROOT+"/images/"+usr.username
    listing = os.listdir(path)
    
    return render_to_response("space/editor/edit_page.html", RequestContext(request,{
              'user':request.user, 'album': album_, 'page':page_, 'listing': listing
    }))
