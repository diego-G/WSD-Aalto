from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('access.views',
    url(r'^login/$', 'login_view'),
    url(r'^logout/$', 'logout_view'),
)
