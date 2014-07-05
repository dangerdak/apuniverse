from django.db import models
from django.template.defaultfilters import slugify

from image_cropping import ImageRatioField
from easy_thumbnails.files import get_thumbnailer
from taggit.managers import TaggableManager


class Gallery(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=40, unique=True)
    project_year = models.IntegerField(max_length=9)
    linked_blog = models.ForeignKey('blog.Post', blank=True, null=True)
    summary = models.TextField(max_length=500, blank=True)
    tags = TaggableManager()

    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField('Last Modified', auto_now=True)

    # TODO not DRY!! (blog models)
    def tag_names(self):
        tag_list = list(self.tags.names())
        return ', '.join(tag_list)
    tag_names.short_description = 'Tags'

    def blog_url(self):
        if (self.linked_blog):
            return self.linked_blog.get_absolute_url()
        return ''
    blog_url.short_description = 'Blog link'

    def number_images(self):
        return self.image_set.count()
    number_images.short_description = 'Number of images'

    class Meta:
        ordering = ['-project_year', '-date_created']
        verbose_name_plural = 'galleries'

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.title)
        super(Gallery, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Image(models.Model):
    title = models.CharField(max_length=200, blank=True)
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

    class Meta:
        ordering = ['thumbnail_position', '-date_created']

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

