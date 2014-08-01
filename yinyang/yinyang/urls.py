from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$','epidemic.views.home'),
    url(r'^NepalMap.svg','epidemic.views.image'),
    url(r'Map','epidemic.views.genmap'),
    # url(r'^$', 'yinyang.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
)
