from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('space.images.views',

    url(r'^$', 'images', name='images'),
    url(r'^delete_image/(?P<file>\w+)', 'delete_image', name='delete_image'),
)