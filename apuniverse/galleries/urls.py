from django.conf.urls import patterns, url

from galleries.views import TagGalleryList, GalleryListView

urlpatterns = patterns('',
    url(r'^$',
        GalleryListView.as_view(),
        name='galleries'),

    # Category views
    url(r'^tags/(?P<tags>\w*)/$',
        TagGalleryList.as_view(),
        name='galleriestags'),
)
