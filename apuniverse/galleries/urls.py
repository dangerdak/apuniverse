from django.conf.urls import patterns, url

from galleries.views import GalleryListView, GalleryListByTag

urlpatterns = patterns('',
    url(r'^$',
        GalleryListView.as_view(),
        name='galleries'),

    # Category views
    url(r'^tags/(?P<tags>\w*)/$',
        GalleryListByTag.as_view(),
        name='galleriestags'),
)
