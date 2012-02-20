from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'pagebook.views.home', name='home'),
    url(r'^(?P<name>\w+)/$', include('space.urls'), name='space'),
    url(r'^access/', include('access.urls'), name='access'),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
