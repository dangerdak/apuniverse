from django.utils import timezone
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=40, unique=True)
    text = models.TextField()

    pub_date = models.DateTimeField('Publishing date', default=timezone.now)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField('Last Modified', auto_now=True)

    def get_absolute_url(self):
        # Hardcoded url in model!!
        date = (self.pub_date.strftime('%Y %b')).lower().split()
        return "/blog/%s/%s/%s" % (date[0],
                                   date[1],
                                   self.slug)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.title
