from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.views import login, logout


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'views.home'),
    # login / logout
    url(r'^login/$', 'views.auth'),
    url(r'^logout/$', 'views.logout_view'),
    
    url(r'^(?P<name>\w+)/$', 'views.albums'),
    # url(r'^wsd/', include('wsd.foo.urls'))
    url(r'^register/$', include('registration.backends.default.urls')),
    
    #create album and page
    url(r'^(?P<name>\w+)/create/$', 'views.create_album'),
    #url(r'(?P<name>\w+)/(?P<album>\w+)/create, 'views.create_page'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
