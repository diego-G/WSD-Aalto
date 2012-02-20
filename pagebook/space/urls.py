from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('space.views',

    url(r'^$', 'home', name='home_user'),
    url(r'^create_album/', 'create', name='create')
    
    #url(r'^(?P<name>\w+)/$', include('space.urls'), name='space'),

)
