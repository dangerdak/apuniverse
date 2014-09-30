from datetime import timedelta

from django.core.urlresolvers import reverse
from django.utils import timezone
from django.db import models

from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager

from blog.managers import PublishedManager

from blog.slugify import unique_slugify


class Post(models.Model):
    verbose_name = 'blog post'
    # MANAGERS
    objects = models.Manager()
    published_objects = PublishedManager()

    # FIELDS
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=40, unique=True)
    text = RichTextField(config_name='blog')
    tags = TaggableManager()
    STATUS_CHOICES = (('published', 'Published'),
                      ('draft', 'Draft'),)
    status = models.CharField(choices=STATUS_CHOICES,
                              default='published',
                              max_length=9)

    pub_date = models.DateTimeField('Date published', default=timezone.now,
                                    editable=False)
    date_created = models.DateTimeField(editable=False)
    last_modified = models.DateTimeField(editable=False)

    # METHODS
    def get_absolute_url(self):
        year, month = (self.pub_date.strftime('%Y %b')).lower().split()
        return reverse('blog-detail', kwargs={'pub_year': year,
                                              'pub_month': month,
                                              'slug': self.slug})

    def save(self, *args, **kwargs):
        status = self.status

        # If draft, set pub_date very far in the future
        if status == 'draft':
            self.pub_date = timezone.now() + timedelta(days=900000)

        if status == 'published' and self.pub_date > timezone.now():
        # ie if status changed from draft to published
        # (as draft is only way pub_date can be in future)
                self.pub_date = timezone.now()

        self.last_modified = timezone.now()
        if not self.id:
        # Newly created object, so set slug and date created
            self.date_created = timezone.now()
            # Ensure slug is unique
            unique_slugify(self, self.title)

        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'blog post'
