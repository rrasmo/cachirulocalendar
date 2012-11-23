from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('events.views',
    url(r'^$', 'home', name='home'),
)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

