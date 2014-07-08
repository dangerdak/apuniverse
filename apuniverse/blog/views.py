from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from taggit.models import Tag

from blog.models import Post


class PostListView(ListView):
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


class PostListByTag(ListView):
    template_name = 'blog/post_list.html'

    def get_queryset(self):
        self.tags = get_object_or_404(Tag, name=self.kwargs['tags'].title())
        return Post.published_objects.filter(tags__name__in=[self.tags])
