from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'blog.views.home', name='home'),
    url(r'^post/(\d+)/$', 'blog.views.single_post', name='post'),
    url(r'^wanted/(\d+)/$', 'blog.views.single_wanted', name='wanted'),

    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
