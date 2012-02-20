# This also imports the include function
from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^Access/', include('Access.urls')),
   
    #create album and page
    url(r'^(?P<name>\w+)/create/$', 'views.create_album'),
    #url(r'(?P<name>\w+)/(?P<album>\w+)/create, 'views.create_page'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)