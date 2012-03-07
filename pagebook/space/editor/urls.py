from django.conf.urls.defaults import patterns, include, url
from django.views.static import *

urlpatterns = patterns('space.editor.views',
    url(r'^choose_image/(?P<nImage>\d+)/$', 'choose_image', name='choose_image'),
    url(r'^asign_image/(?P<nImage>\d+)/(?P<name_file>[\w|\W]+\.\w+)$', 'asign_image', name='asign_image'),
    url(r'^choose_image/(?P<nImage>\d+)/upload_image_flickr/$', 'upload_image_flickr', name='upload_image_flickr'),                
)