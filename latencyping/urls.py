from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'ping.views.index'),
    url(r'^ping/([0-9]+)/$', 'ping.views.ping'),
    url(r'^upload/([^/]+)/$', 'ping.views.upload'),
    url(r'^delete/([0-9]+)/$', 'ping.views.delete'),

    #url('^accounts/', include('django.contrib.auth.urls')),
    url('^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()
