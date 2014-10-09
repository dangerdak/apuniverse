from django.conf.urls import patterns, url

from blog.views import (PostListView,
                        PostDetailView,
                        PostYearArchiveView,
                        PostListByTag)

urlpatterns = patterns('',
    # Index view
    url(r'^$',
        PostListView.as_view(),
        name='blog',
        ),

    # Detail view
    url(r'^(?P<pub_year>\d{4})/(?P<pub_month>\w{3})/(?P<slug>[a-zA-Z0-9-]+)/$',
        PostDetailView.as_view(),
        name='blog-detail',
        ),

    # Yearly archive view
    url(r'^(?P<year>\d{4})/$',
        PostYearArchiveView.as_view(),
        name='blogarchive'
        ),

    # Category view
    url(r'^tags/(?P<tags>\w*)/$',
        PostListByTag.as_view(),
        name='blogtags',
        ),
)
