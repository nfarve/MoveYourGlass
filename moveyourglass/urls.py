from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'moveyourglass.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^register/', include('registration.urls')),
    url(r'^process/', include('process.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^id/', include('getId.urls'))
    url(r'^summary/(?P<userid>[\w\-]+)', 'process.views.summary')
    url(r'^summary/(?P<userid>[\w\-]+)/glass', 'process.views.glass')
)
