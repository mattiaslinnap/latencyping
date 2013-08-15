from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'ping.views.index'),
    url(r'^ping/([0-9]+)/$', 'ping.views.ping'),
    url(r'^upload/([^/]+)/$', 'ping.views.upload'),
)
