from django.conf.urls import patterns, url
from django.views.generic import DetailView

from blog.views import PostListView, PostListByTag
from blog.models import Post

urlpatterns = patterns('',
    # Index
    url(r'^$',
        PostListView.as_view(),
        name='blog',
        ),
    # Individual posts
    url(r'^(?P<pub_year>\d{4})/(?P<pub_month>\w{3})/(?P<slug>[a-zA-Z0-9-]+)/$',
        DetailView.as_view(model=Post,),
        ),
    # Category views
    url(r'^tags/(?P<tags>\w*)/$',
        PostListByTag.as_view(),
        name='blogtags',
        ),
)
