from django.conf.urls import patterns, include, url

from django.views.generic import ListView

from django.contrib import admin

from builds.models import Build
from builds.views import builds_by_project

admin.autodiscover()



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'build_manager.views.home', name='home'),
    # url(r'^build_manager/', include('build_manager.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
     url(r'^admin/', include(admin.site.urls)),
    
     url(r'^(?P<project_name>\w+)/$', builds_by_project),
 
)
