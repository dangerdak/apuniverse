from django.conf.urls import patterns, url
from django.views.generic import ListView
from blog.models import Post

urlpatterns = patterns('',
    # Index
    url('^$', ListView.as_view(
        model=Post,
        )),
)
