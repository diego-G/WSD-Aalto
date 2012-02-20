from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('views',
    url(r'^$', 'home'),
    
    # login / logout
    url(r'^login/$', 'auth'),
    url(r'^logout/$', 'logout_view'),
    
    url(r'^(?P<name>\w+)/$', 'albums'),
)
