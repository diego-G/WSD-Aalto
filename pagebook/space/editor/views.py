from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from space.models import Album, Page, Image, AlbumForm, PageForm
from django.core.context_processors import csrf

from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.shortcuts import render_to_response
from django.template import Context, RequestContext

from settings import MEDIA_ROOT, MEDIA_URL
import os
from urlparse import urlparse
from urllib import urlretrieve

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
    set_images = page_.images.all().order_by('pos')
    path = MEDIA_ROOT+"/images/"+usr.username
    try:
        listing = os.listdir(path)
    except OSError:
        listing = ''
    
    return render_to_response("space/editor/edit_page.html", RequestContext(request,{
              'user':request.user, 'album': album_, 'page':page_, 'set_images': set_images,
    }))
    
def choose_image(request, name, album, page, nImage):
    nImage = int(nImage)
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
        listing = []
    return render_to_response("space/editor/choose_image.html", RequestContext(request,{
             'user':request.user, 'album': album_, 'page':page_, 'listing': listing, 'nImage': nImage
    }))
    
def asign_image(request, name, album, page, nImage, name_file):
    
    try:
        usr = User.objects.get(username=name)
    except User.DoesNotExist:
        raise Http404
    try:
        album_ = Album.objects.get(user=usr, id=album)
    except Album.DoesNotExist:
        raise Http404
    page_ = Page.objects.get(album=album_, number=page)
    
    path = MEDIA_URL+"/images/"+usr.username+"/"+name_file

    image = Image(name=name_file, file=path, pos=nImage)
    image.save()
  
    filtered = page_.images.filter(pos=nImage)
    for filt in filtered:
        page_.images.remove(filt)
    page_.save()
        
    page_.images.add(image)
    page_.save()
    
    return HttpResponseRedirect("../../")

def upload_image_flickr(request, name, album, page, nImage):
    url = request.GET.get('url')  
    filename = os.path.basename(url)
    urlretrieve(url, MEDIA_ROOT+"/images/"+name+"/"+filename)
    
    return HttpResponseRedirect("../../../asign_image/"+nImage+"/"+filename)    
