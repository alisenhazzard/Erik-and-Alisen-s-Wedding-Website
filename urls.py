from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'veinterface.views.home', name='home'),
    # url(r'^veinterface/', include('veinterface.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #-------------------------------------------------------------------------
    #Base Pages
    #-------------------------------------------------------------------------
    #Home
    url(r'^$', 'website.views.page_home', 
        name='home'),
    url(r'^home[/]$', 'website.views.page_home', 
        name='home'),

    url(r'^our_story[/]$', 'website.views.page_our_story', 
        name='our_story'),
    url(r'^wedding_party[/]$', 'website.views.page_wedding_party', 
        name='wedding_party'),
    url(r'^guest_info[/]$', 'website.views.page_guest_info', 
        name='guest_info'),
    url(r'^registry[/]$', 'website.views.page_registry', 
        name='registry'),

    #-------------------------------------------------------------------------
    #Guest book
    #-------------------------------------------------------------------------
    url(r'^guest_book[/]$', 'website.views.page_guest_book', 
        name='guest_book'),

    #-------------------------------------------------------------------------
    #Github Hook
    #-------------------------------------------------------------------------
    url(r'^github[/]$', 'website.views.github_hook', 
        name='github'),

)

if settings.DEBUG:
    urlpatterns += patterns('',
    (r'^static/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )

