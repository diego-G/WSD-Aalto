from django.conf.urls.defaults import patterns, include, url
from django.views.static import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'pagebook.views.home', name='home'),
    url(r'^/login_error/$', 'login_error', name='login_error'),
    url(r'^social_auth/', include('social_auth.urls')),
    url(r'^access/', include('access.urls'), name='access'),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                 {'document_root': settings.MEDIA_ROOT}),
    url(r'^(?P<name>\w+)/', include('space.urls'), name='space'),
)
