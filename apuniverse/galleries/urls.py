from django.conf.urls import patterns, url

from galleries.views import (GalleryListView,
                             GalleryDetailView,
                             GalleryListByTag,
                             GalleryYearArchiveView)

urlpatterns = patterns('',
    url(r'^$',
        GalleryListView.as_view(),
        name='galleries'),

    # Detail view
    url(r'^(?P<slug>[a-zA-Z0-9-]+)/$',
        GalleryDetailView.as_view(),
        name='gallery-detail',
        ),

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
