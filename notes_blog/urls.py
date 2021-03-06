from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'notes_blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'blog.views.index', name='index'),
    url(r'^(?P<slug>[\w\-]+)/$', 'blog.views.post'),
    url(r'^redactor/', include('redactor.urls')),
)
