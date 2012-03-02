from django.conf.urls.defaults import patterns, include, url
from django.views.static import *

from django.conf.urls.defaults import *

urlpatterns = patterns('',
	url(r'^$', 'django_openid_consumer.views.begin'),
    url(r'^complete/$', 'django_openid_consumer.views.complete'),
    url(r'^signout/$', 'django_openid_consumer.views.signout'),
)
