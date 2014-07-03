from endless_pagination.views import AjaxListView

from galleries.models import Image, Gallery


class IndexView(AjaxListView):
    model = Gallery

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['gallery_list'] = []
        for instance in Gallery.objects.all():
            context['gallery_list'].append({
                'title': instance.title,
                'image_list': Image.objects.filter(gallery__title=instance.title),
                })
        return context
