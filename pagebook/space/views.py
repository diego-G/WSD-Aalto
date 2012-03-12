from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, RequestContext
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.contrib.auth import *
from django.http import Http404
from django.contrib.auth.models import User
from models import Album, Page, Image, AlbumForm, PageForm
from django.core.context_processors import csrf
from django.utils import simplejson

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from settings import MEDIA_ROOT, MEDIA_URL, STATIC_URL
import os

@login_required
def home(request, name):
    """
    It shows the albums collection of the authenticated user.
    Also redirect to another user space through the finder.
    If the user doesn't exist in the database, It shows the errors and exceptions properly .
    """ 
    c = {}
    c.update(csrf(request))
    try:
        usr = User.objects.get(username=name)
    except User.DoesNotExist:
        raise Http404
    albums = Album.objects.filter(user=usr)
    
    if request.method == 'POST':
        another_user = request.POST.get('another_user')
        try:
             exist = User.objects.get(username=another_user)
        except User.DoesNotExist:
            return render_to_response("space/user_not_exist.html", RequestContext(request,{}))
        return HttpResponseRedirect("/" + another_user + "/")
    
    if request.user != usr:
         albums = Album.objects.filter(user=usr, private=False)
    return render_to_response("space/collections.html", c, RequestContext(request,{
        'user':request.user, 'owner':usr, 'albums':albums
    }))

def create_album(request, name):
    """
    The creation of new album through a form according to models.py
    """     
    if request.user.username == name:   
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
    else:
        raise Http404


def delete_album(request, name, album):
    """
    Deletion of the required album
    """    
    usr = User.objects.get(username=request.user.username)
    Album.objects.filter(user=usr, id=album).delete()
    return HttpResponseRedirect("/")

@login_required
def show_album(request, name, album):
    """
    Showing the pages of the required album.
    It finds the album in the database throwing the necessary exceptions.
    """   
    try:
        usr = User.objects.get(username=name)
    except User.DoesNotExist:
        raise Http404
    try:
        album_ = Album.objects.get(user=usr, id=album)
    except Album.DoesNotExist:
        raise Http404
    pages = Page.objects.filter(album=album_)
    return render_to_response("space/album.html",
            RequestContext(request,{'user':request.user, 'owner':usr, 'pages':pages, 'album':album_})
    )

def create_page(request, name, album):
    """
    The creation of new page of an album. Layout of the page is chosen. 
    It attach the emptySpace image to each gap of the page, the number of times depending of the layout.
    """      
    if request.user.username == name:
        if request.method == 'POST': # If the form has been submitted...
            try:
                usr = User.objects.get(username=name)
                rel_album = Album.objects.get(user=usr,id=album)
                rel_page = Page.objects.filter(album=rel_album.id)
                length = len(rel_page)
                layout_ = request.POST.get("layout")
                page = Page(album=rel_album,number=int(length)+1,layout=int(layout_),)
                page.save()
                
                for cont in range(int(layout_)): 
                    img = Image(name="emptySpace.gif",pos=cont+1, 
                        file= STATIC_URL+"images/emptySpace.gif")
                    img.save()
                    page.images.add(img)
                    page.save()
                
            except Album.DoesNotExist:
                raise Http404
            
            form = PageForm(request.POST, instance=page) # A form bound to the POST data
    
            if form.is_valid(): # All validation rules pass
                # Process the data in form.cleaned_data
                form.save()
                
                return HttpResponseRedirect('../') # Redirect after POST
        else:
            form = PageForm() # An unbound form
    
        return render_to_response('space/create_page.html', RequestContext(request,{
            'form': form,
        }))
    else:
        raise Http404

    
def delete_page(request, name, album, page):
    """
    It deletes the required page and redirect to the adequate view.
    """
    usr = User.objects.get(username=request.user.username)
    album_ = Album.objects.filter(user=usr, id=album)
    page = Page.objects.get(album=album_, id=page)
    num_pag = page.number
    page.delete()
    pag_mod = Page.objects.filter(album=album_, number__gt=num_pag)
    for pag in pag_mod:
        pag.number -= 1
        pag.save()
    return HttpResponseRedirect("../../")

@login_required
def pages(request, name, album):
    """
    This view shows the required page. 
    Here is where is captured the Ajax request to display the next or previous page of the album.
    """
    if request.method == 'GET':
        page = request.GET.get('page')
    else:
        page = 1;
    try:
        usr = User.objects.get(username=name)
    except User.DoesNotExist:
        raise Http404
    try:
        album_ = Album.objects.get(user=usr, id=album)
    except Album.DoesNotExist:
        raise Http404
    page_ = Page.objects.get(album=album_,number=page)
    try:
        page_back = Page.objects.get(album=album_,number=int(page)-1).number
    except Page.DoesNotExist:
        page_back = -1
    try:
        page_next = Page.objects.get(album=album_,number=int(page)+1).number
    except Page.DoesNotExist:
        page_next = -1
    imgs = page_.images.all().order_by('pos')
    print request.is_ajax()
    if request.is_ajax():
        return render_to_response("space/pages_content.html", RequestContext(request,{
                                'user':request.user, 'owner':usr, 'album': album_, 'page':page_, 'page_back':page_back, 
                                'page_next':page_next, 'set_images': imgs
        }))
    else:
        return render_to_response("space/pages.html", RequestContext(request,{
                                'user':request.user, 'owner':usr, 'album': album_, 'page':page_, 'page_back':page_back, 
                                'page_next':page_next, 'set_images': imgs
        }))
      
@login_required
def change_pass(request, name):
    """
    This view permits the user to change its password.
    """
    if request.user.username == name:
        form = PasswordChangeForm(request.user)
        if request.POST:
                form = PasswordChangeForm(request.user,request.POST)
                if form.is_valid():
                    form.save()
                    return HttpResponseRedirect('done/')
        return render_to_response('space/change_pass_form.html', {
                'form': form } , context_instance=RequestContext(request)
            )
    else:
        raise Http404
  
def change_pass_done(request, name):
    """
    Display if the password has changed successfully.
    """
    return render_to_response('space/change_pass_done.html',
             context_instance=RequestContext(request))
    
def render_javascript(request, name):
    return render_to_response("js/js_page.js", mimetype="text/javascript")

@login_required
def edit_album(request, name, album):
    """
    Let the user changes the name of an existing album.
    It's performed by using a javascript function and jquery library.
    """
    if request.user.username == name:   
        c = {}
        c.update(csrf(request))
        usr = User.objects.get(username=name)
        try:
            album_ = Album.objects.get(user=usr, id=album)
        except Album.DoesNotExist:
            album_ = Album()
        if request.method == 'POST': # If the form has been submitted...
            new_name = request.POST.get('name')
            album_.name = new_name
            album_.save()
            return HttpResponse('<button type="button" id="edit_button">Change Album\'s name</button>')
            
        return render_to_response('space/edit_album.html', RequestContext(request,{
                'user':request.user, 'owner':usr, 'album':album_
                    }))
        
    else:
        raise Http404

def lookup_users(request, name):
    """
    This view is used to auto-complete the most relevant results in the finder.
    Look for the names in the database and display them in the page below the finder.
    It's performed by using a javascript function and jquery library.
    """
    # Default return list
    results = []
    if request.method == "GET":
        if request.GET.has_key(u'query'):
            value = request.GET[u'query']
            # Ignore queries shorter than length 3
            if len(value) > 0:
                model_results = User.objects.filter(username__icontains=value)
                results = [ x.username for x in model_results ]
                print results
    json = simplejson.dumps(results)
    return HttpResponse(json, mimetype='application/json')
