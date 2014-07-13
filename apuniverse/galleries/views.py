from django.shortcuts import get_object_or_404
from django.views.generic.dates import YearArchiveView
# from django.db.models import Count

from taggit.models import Tag
from endless_pagination.views import AjaxListView

from galleries.models import Image, Gallery


class MonthArchiveMixin(object):
    """
    Mixin adds by-month archive info to context.
    Adds 'by_month', a list of tuples in the format
    (month, [object_list]).
    Dates in descending order.
    """

    def get_context_data(self, **kwargs):
        context = super(MonthArchiveMixin, self).get_context_data(**kwargs)

        # Determine queryset to be used
        if self.queryset:
            qs = self.queryset
        elif self.model.published_objects:
            qs = self.model.published_objects.all()
        else:
            qs = self.model.objects.all()

        print(self.kwargs['year'])

        # Get all objects for the year
        objects = qs.filter(pub_date__year=self.kwargs['year'])

        # Get all months in the year which contain an object
        all_month_dates = objects.datetimes('pub_date', 'month', 'DESC')
        by_month = []
        for date in all_month_dates:
            # Objects for each month
            # ordered by pub_date (see model meta class)
            month = date.month
            by_month.append((date, objects.filter(pub_date__month=month)))
        context['by_month'] = by_month
        return context


class GalleryListView(AjaxListView):
    queryset = Gallery.published_objects.all()

    def get_context_data(self, **kwargs):
        context = super(GalleryListView, self).get_context_data(**kwargs)
        # Add images to context
        context['gallery_list'] = []
        # So that the context contains the images associated with each gallery
        for instance in self.queryset:
            context['gallery_list'].append({
                'title': instance.title,
                'image_list': Image.objects.filter(
                    gallery__title=instance.title),
                'tags': instance.tags,
                })

        # Add archive links to context
        all_year_dates = self.queryset.datetimes('pub_date', 'year', 'DESC')
        archive_links = []
        for date in all_year_dates:
            year = date.year
            year_count = self.queryset.filter(pub_date__year=year).count()
            archive_links.append((year, year_count))
        context['archive_links'] = archive_links

        return context


class GalleryYearArchiveView(MonthArchiveMixin, YearArchiveView):
    model = Gallery
    date_field = 'pub_date'
    make_object_list = True
    allow_empty = True
    allow_future = False


class GalleryListByTag(AjaxListView):
    template_name = 'galleries/gallery_list.html'

    def get_queryset(self):
        self.tags = get_object_or_404(Tag, name=self.kwargs['tags'].title())
        return Gallery.published_objects.filter(tags__name__in=[self.tags])

    def get_context_data(self, **kwargs):
        context = super(GalleryListByTag, self).get_context_data(**kwargs)
        context['gallery_list'] = []
        # So that the context contains the images associated with each gallery
        for instance in self.get_queryset():
            context['gallery_list'].append({
                'title': instance.title,
                'image_list': Image.objects.filter(
                    gallery__title=instance.title),
                'tags': instance.tags,
                })
        return context
