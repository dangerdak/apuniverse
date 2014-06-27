from django.conf.urls import patterns, url

from galleries.views import IndexView

urlpatterns = patterns('',
        url(r'^$',
            IndexView.as_view(),
            name='galleries'),
        )
