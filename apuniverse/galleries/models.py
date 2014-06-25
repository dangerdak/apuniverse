from django.db import models

from image_cropping import ImageRatioField


class Gallery(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=40, unique=True)
    project_year = models.IntegerField(max_length=9)
    blog_link = models.URLField('Associated blog (optional)',
                                blank=True)
    summary = models.TextField(max_length=500, blank=True)

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
    date = models.DateField(blank=True)
    medium = models.CharField(max_length=200, blank=True)
    size = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to='media/')
    cropping = ImageRatioField('image', '100x100')

    gallery = models.ForeignKey(Gallery)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField('Last Modified', auto_now=True)

    def __str__(self):
        return self.title
