from datetime import timedelta

from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone

from image_cropping import ImageRatioField
from easy_thumbnails.files import get_thumbnailer
from taggit.managers import TaggableManager

from galleries.managers import PublishedManager


class Gallery(models.Model):
    # MANAGERS
    objects = models.Manager()
    published_objects = PublishedManager()

    # FIELDS
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=40, unique=True)
    project_year = models.IntegerField(max_length=9)
    linked_blog = models.ForeignKey('blog.Post', blank=True, null=True)
    summary = models.TextField(max_length=500, blank=True)
    tags = TaggableManager()
    STATUS_CHOICES = (('published', 'Published'),
                      ('draft', 'Draft'),)
    status = models.CharField(choices=STATUS_CHOICES,
                              default='published',
                              max_length=9)

    pub_date = models.DateTimeField('Date published', default=timezone.now,
                                    editable=False)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField('Last Modified', auto_now=True)

    # METHODS
    def blog_url(self):
        if (self.linked_blog):
            return self.linked_blog.get_absolute_url()
        return ''
    blog_url.short_description = 'Blog link'

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
            self.slug = slugify(self.title)

        super(Gallery, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']
        verbose_name_plural = 'galleries'


class Image(models.Model):
    # FIELDS
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=40, unique=True)
    date = models.DateField(blank=True, null=True)
    medium = models.CharField(max_length=200, blank=True)
    size = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to='images/')
    thumbnail = ImageRatioField('image', '100x100')

    gallery = models.ForeignKey(Gallery)
    thumbnail_position = models.PositiveSmallIntegerField(
        blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField('Last Modified', auto_now=True)

    # METHODS
    def thumbnail_url(self):
        url = get_thumbnailer(self.image).get_thumbnail({
            'size': (100, 100),
            'box': self.thumbnail,
            'crop': True,
            'detail': True,
            }).url
        return url
    # Disable escaping of html
    thumbnail_url.allow_tags = True

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.title)
        super(Image, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['thumbnail_position', '-date_created']
