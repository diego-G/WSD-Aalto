from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('space.views',

    url(r"^js/js_page.js", 'render_javascript', name='render_javascript'),
    url(r'^$', 'home', name='home_user'),
    url(r'^create_album/$', 'create_album', name='create_album'),
    url(r'^delete_album/(?P<album>\d+)/', 'delete_album', name='delete_album'),
    url(r'^(?P<album>\d+)/$', 'show_album', name='show_album'),
    url(r'^(?P<album>\d+)/create_page/', 'create_page', name='create_page'),
    url(r'^(?P<album>\d+)/delete_page/(?P<page>\d+)/', 'delete_page', name='delete_page'),
    #url(r'^(?P<name>\w+)/$', include('space.urls'), name='space'),
    url(r'^(?P<album>\d+)/view/', 'pages', name='pages'),
    url(r'^(?P<album>\d+)/(?P<page>\d+)/', 'render_page', name='render_page'),
    
    url(r'^images/', include('space.images.urls'), name='images'),
        
    url(r'^change_pass/$', 'change_pass', name='change_pass'),
    url(r'^change_pass/done/$', 'change_pass_done'),
    
)
