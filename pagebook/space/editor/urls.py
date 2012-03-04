from django.conf.urls.defaults import patterns, include, url
from django.views.static import *

urlpatterns = patterns('',
    url(r'^$', 'edit_page', name='edit_page'),                 
)