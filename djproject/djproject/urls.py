from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'djapp.views.hello_world', name='hello_world'),
    url(r'^list/$', 'djapp.views.list', name='list'),
    url(r'^admin/', include(admin.site.urls)),
)
