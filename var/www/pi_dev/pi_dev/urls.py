from django.conf.urls import patterns, include, url
from control import urls as conurls
from pi import urls as piurls

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pi_dev.views.home', name='home'),
    # url(r'^pi_dev/', include('pi_dev.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^control/', include(conurls)),
    url(r'^pi/', include(piurls)),
    (r'^$','pi.views.index'),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve'),
)
