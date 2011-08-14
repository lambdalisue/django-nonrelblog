from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    # Required to enable background tasks
    url(r'^_ah/warmup$', 'djangoappengine.views.warmup'),
    url(r'^', include('apps.simpleblogs.urls')),
    url(r'^registration/', include('django.contrib.auth.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
