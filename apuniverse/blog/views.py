from django.views.generic import ListView
from django.views.generic.dates import YearArchiveView, MonthArchiveView
from django.shortcuts import get_object_or_404
from taggit.models import Tag

from blog.models import Post


class MonthArchiveMixin(object):
    """
    Mixin adds by-month archive info to context.
    Adds 'by_year', a list of tuples in the format (year, by_month)
    where 'by_month is a list of tuples in the format
    (month, [post_list]). I.e. by_year = [(year, (month, [post_list]))...]
    Dates in descending order.
    """

    def get_context_data(self, **kwargs):
        context = super(MonthArchiveMixin, self).get_context_data(**kwargs)

        if self.queryset:
            qs = self.queryset
        elif self.model.published_objects:
            qs = self.model.published_objects.all()
        else:
            qs = self.model.objects.all()

        all_year_dates = qs.datetimes('pub_date', 'year', 'DESC')
        by_year = []
        for year_date in all_year_dates:
            year = year_date.year
            # Get all posts for the year
            posts = qs.filter(pub_date__year=year)

            # Get all months in the year which contain a post
            all_month_dates = posts.datetimes('pub_date', 'month', 'DESC')
            by_month = []
            for date in all_month_dates:
                # Posts for each month
                # ordered by pub_date (see model meta class)
                month = date.month
                by_month.append((date, posts.filter(pub_date__month=month)))
            by_year.append((year, by_month))
        context['by_year'] = by_year
        return context


class PostListView(MonthArchiveMixin, ListView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['post_list'] = []
        for instance in Post.published_objects.all():
            context['post_list'].append({
                'title': instance.title,
                'text': instance.text,
                'pub_date': instance.pub_date,
                'url': instance.get_absolute_url(),
                'tags': instance.tags,
            })
        return context


class PostYearArchiveView(MonthArchiveMixin, YearArchiveView):
    model = Post
    date_field = 'pub_date'
    make_object_list = True
    allow_empty = True
    allow_future = False


class PostMonthArchiveView(MonthArchiveView):
    queryset = Post.published_objects.all()
    date_field = 'pub_date'
    make_object_list = True
    allow_empty = True
    allow_future = False


class PostListByTag(ListView):
    template_name = 'blog/post_list.html'

    def get_queryset(self):
        self.tags = get_object_or_404(Tag, name=self.kwargs['tags'].title())
        return Post.published_objects.filter(tags__name__in=[self.tags])
