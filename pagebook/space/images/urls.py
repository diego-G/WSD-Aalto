from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('space.images.views',

    url(r'^$', 'images', name='images'),
)