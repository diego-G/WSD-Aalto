from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('access.views',
    url(r'^login/$', 'login_view', name='login_view'),
    url(r'^logout/$', 'logout_view', name='logout_view'),
    url(r'^register/$', 'register' , name='register'),
)
