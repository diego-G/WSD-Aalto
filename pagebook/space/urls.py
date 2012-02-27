from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('space.views',

    url(r'^$', 'home', name='home_user'),
    url(r'^create_album/$', 'create_album', name='create_album'),
    url(r'^delete_album/(?P<album>\d+)/', 'delete_album', name='delete_album'),
    url(r'^(?P<album>\d+)/$', 'show_page', name='show_page'),
    url(r'^(?P<album>\d+)/create_page/', 'create_page', name='create_page'),
    url(r'^(?P<album>\d+)/delete_page/(?P<page>\d+)/', 'delete_page', name='delete_page'),
    #url(r'^(?P<name>\w+)/$', include('space.urls'), name='space'),

)
