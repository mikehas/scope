from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'scopesitch.views.home', name='home'),
    # url(r'^scopesitch/', include('scopesitch.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    # Create a url
    url(r'^projects/$', 'directory.views.index'),
    url(r'^project/(?P<project_id>\d+)/$', 'directory.views.detail'),
    url(r'^location/$', 'directory.views.location_index'),
    url(r'^location/(?P<location_id>\d+)/$', 'directory.views.location_detail'),
    
    url(r'^manage/add$', 'directory.views.manage_add'),
    
)
