from django.utils import timezone
from django.db import models
from django.template.defaultfilters import slugify

from taggit.managers import TaggableManager


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=40, unique=True)
    text = models.TextField()
    tags = TaggableManager()

    pub_date = models.DateTimeField('Date published', default=timezone.now)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField('Last Modified', auto_now=True)

    def get_absolute_url(self):
        # TODO Hardcoded url in model!!
        date = (self.pub_date.strftime('%Y %b')).lower().split()
        return "/blog/%s/%s/%s" % (date[0],
                                   date[1],
                                   self.slug)

    # TODO not DRY!! (gallery models)
    def tag_names(self):
        tag_list = list(self.tags.names())
        return ', '.join(tag_list)
    tag_names.short_description = 'Tags'

    def is_published(self):
        if self.pub_date > timezone.now():
            return False
        return True
    is_published.boolean = True
    is_published.short_description = 'Published?'
    is_published.admin_order_field = 'pub_date'

    # TODO not dry
    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.title
