from django.views.generic import DetailView
from django.views.generic.dates import YearArchiveView
from django.shortcuts import get_object_or_404

from taggit.models import Tag
from endless_pagination.views import AjaxListView

from blog.models import Post


class MonthArchiveMixin(object):
    """
    Mixin adds by-month archive info to context.
    Adds 'by_month', a list of tuples in the format
    (month, [post_list]).
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

        # Get all posts for the year
        objects = qs.filter(pub_date__year=self.kwargs['year'])

        # Get all months in the year which contain a post
        all_month_dates = objects.datetimes('pub_date', 'month', 'DESC')
        by_month = []
        for date in all_month_dates:
            # Posts for each month
            # ordered by pub_date (see model meta class)
            month = date.month
            by_month.append((date, objects.filter(pub_date__month=month)))
        context['by_month'] = by_month
        return context


class PostListView(AjaxListView):
    queryset = Post.published_objects.all()

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        # Add archive links to context
        all_year_dates = self.queryset.datetimes('pub_date', 'year', 'DESC')
        archive_links = []
        for date in all_year_dates:
            year = date.year
            year_count = self.queryset.filter(pub_date__year=year).count()
            archive_links.append((year, year_count))
        context['archive_links'] = archive_links
        return context


class PostDetailView(DetailView):
    queryset = Post.published_objects.all()

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        # Add archive links to context
        all_year_dates = self.queryset.datetimes('pub_date', 'year', 'DESC')
        archive_links = []
        for date in all_year_dates:
            year = date.year
            year_count = self.queryset.filter(pub_date__year=year).count()
            archive_links.append((year, year_count))
        context['archive_links'] = archive_links
        return context


class PostYearArchiveView(MonthArchiveMixin, YearArchiveView):
    queryset = Post.published_objects.all()
    date_field = 'pub_date'
    make_object_list = True
    allow_empty = True
    allow_future = False

    def get_context_data(self, **kwargs):
        context = super(PostYearArchiveView, self).get_context_data(**kwargs)
        # Add archive links to context
        all_year_dates = self.queryset.datetimes('pub_date', 'year', 'DESC')
        archive_links = []
        for date in all_year_dates:
            year = date.year
            year_count = self.queryset.filter(pub_date__year=year).count()
            archive_links.append((year, year_count))
        context['archive_links'] = archive_links
        return context


class PostListByTag(AjaxListView):
    queryset = Post.published_objects.all()
    template_name = 'blog/post_list.html'

    def get_queryset(self, **kwargs):
        self.tags = get_object_or_404(Tag, name=self.kwargs['tags'].title().replace('-', ' '))
        return Post.published_objects.filter(tags__name__in=[self.tags])

    def get_context_data(self, **kwargs):
        context = super(PostListByTag, self).get_context_data(**kwargs)
        # Add archive links to context
        all_year_dates = self.queryset.datetimes('pub_date', 'year', 'DESC')
        archive_links = []
        for date in all_year_dates:
            year = date.year
            year_count = self.queryset.filter(pub_date__year=year).count()
            archive_links.append((year, year_count))
        context['archive_links'] = archive_links
        return context
