from django.conf.urls import patterns, include, url

from django.contrib import admin
#from blog import search 
#from blog import search2
from article.views import RSSFeed

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^$','install.views.index',name='index'),
    #url(r'^install','install.views.install',name='install'),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^index/$','blog.views.index'),

    #url(r'^search-form/$',search.search_form),
    #url(r'^search/$',search.search),
    #url(r'^search-post/$',search2.search_post),
    url(r'^$', 'article.views.home', name = 'home'),
    url(r'^(?P<id>\d+)/$', 'article.views.detail', name='detail'),
    url(r'^archives/$', 'article.views.archives', name = 'archives'),
    url(r'^aboutme/$', 'article.views.about_me', name = 'about_me'),
    url(r'^tag/(?P<tag>\w+)/$', 'article.views.search_tag', name = 'search_tag'),
    url(r'^search/$','article.views.blog_search', name = 'search'),
    url(r'^feed/$', RSSFeed(), name = "RSS"),
)
