# from django.conf.urls import patterns, include, url
from django.conf.urls import *
from pi_dev.views import Pi_Index
from pi_dev.views import hello

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pi_dev.views.home', name='home'),
    # url(r'^pi_dev/', include('pi_dev.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    (r'^$',Pi_Index),
    ('^pi/$', Pi_Index),
    ('^hello/$', hello),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve'),
)
