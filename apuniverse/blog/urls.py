from django.conf.urls import patterns, url
from django.views.generic import ListView, DetailView

from blog.models import Post

urlpatterns = patterns('',
    # Index
    url(r'^$',
        ListView.as_view(model=Post,),
        name='blog',
        ),
    # Individual posts
    url(r'^(?P<pub_year>\d{4})/(?P<pub_month>\d{1,2})/(?P<slug>[a-zA-Z0-9-]+)/$',
        DetailView.as_view(model=Post,),
        ),
)
