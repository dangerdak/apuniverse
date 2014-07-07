from django.shortcuts import get_object_or_404

from taggit.models import Tag
from endless_pagination.views import AjaxListView

from galleries.models import Image, Gallery


class GalleryListView(AjaxListView):
    model = Gallery

    def get_context_data(self, **kwargs):
        context = super(GalleryListView, self).get_context_data(**kwargs)
        context['gallery_list'] = []
        # So that the context contains the images associated with each gallery
        for instance in Gallery.objects.all():
            context['gallery_list'].append({
                'title': instance.title,
                'image_list': Image.objects.filter(gallery__title=instance.title),
                'tags': instance.tags,
                })
        return context


class TagGalleryList(AjaxListView):
    template_name = 'galleries/gallery_list.html'

    def get_queryset(self):
        self.tags = get_object_or_404(Tag, name=self.kwargs['tags'].title())
        return Gallery.objects.filter(tags__name__in=[self.tags])

    def get_context_data(self, **kwargs):
        context = super(TagGalleryList, self).get_context_data(**kwargs)
        context['gallery_list'] = []
        # So that the context contains the images associated with each gallery
        for instance in self.get_queryset():
            context['gallery_list'].append({
                'title': instance.title,
                'image_list': Image.objects.filter(gallery__title=instance.title),
                'tags': instance.tags,
                })
        return context
