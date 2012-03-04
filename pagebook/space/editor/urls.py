from django.conf.urls.defaults import patterns, include, url
from django.views.static import *

urlpatterns = patterns('space.editor.views',
    url(r'^$', 'edit_page', name='edit_page'),
    url(r'^choose_image/$', 'choose_image', name='choose_image'),            
)