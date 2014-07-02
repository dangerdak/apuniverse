from django.db import models

from image_cropping import ImageRatioField
from easy_thumbnails.files import get_thumbnailer
from taggit.managers import TaggableManager


class Gallery(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=40, unique=True)
    project_year = models.IntegerField(max_length=9)
    blog_link = models.URLField('Associated blog (optional)',
                                blank=True)
    summary = models.TextField(max_length=500, blank=True)
    tags = TaggableManager()

    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField('Last Modified', auto_now=True)

    class Meta:
        ordering = ['-project_year', '-date_created']
        verbose_name_plural = 'galleries'

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
    position = models.IntegerField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField('Last Modified', auto_now=True)

    class Meta:
        ordering = ['position', '-date_created']

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

    def __str__(self):
        return self.title

