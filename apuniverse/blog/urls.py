from django.conf.urls import patterns, url
from django.views.generic import ListView
from blog.models import Post

urlpatterns = patterns('',
    # Index
    url('^(?P<page>\d+)?/?$', ListView.as_view(
        model=Post,
        )),
)
