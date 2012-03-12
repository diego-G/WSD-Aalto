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
def choose_image(request, name, album, page, nImage):
    """
    The images of the database are presented to assign one of them to a page.
    """ 
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

    if request.user==usr:  
        return render_to_response("space/editor/choose_image.html", RequestContext(request,{
                 'user':request.user, 'album': album_, 'page':page_, 'listing': listing, 'nImage': nImage
        }))
    else:
        raise Http404

@login_required    
def asign_image(request, name, album, page, nImage, name_file):
    """
    The chosen image is attach to the corresponding page.
    It returns to the page-show.
    """     
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
    
    return HttpResponseRedirect("/"+ name + "/" + album + "/view/?page=" + page)

@login_required
def upload_image_flickr(request, name, album, page, nImage):
    """
    It gives to the user the chance of choosing an image of any topic.
    """  
    url = request.GET.get('url')
    filename = os.path.basename(url)
    dir = MEDIA_ROOT+"/images/"+name+"/"+filename
    
    urlretrieve(url, dir) 
    os.chmod(dir, 0644)
    
    return HttpResponseRedirect("../../../asign_image/"+nImage+"/"+filename)    
