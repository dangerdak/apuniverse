from django.conf.urls import patterns, url

from galleries.views import (GalleryListView,
                             GalleryListByTag,
                             GalleryYearArchiveView)

urlpatterns = patterns('',
    url(r'^$',
        GalleryListView.as_view(),
        name='galleries'),

    # Yearly archive view
    url(r'^(?P<year>\d{4})/$',
        GalleryYearArchiveView.as_view(),
        name='gallery_year_archive'
        ),

    # Category view
    url(r'^tags/(?P<tags>\w*)/$',
        GalleryListByTag.as_view(),
        name='galleriestags'),
)
