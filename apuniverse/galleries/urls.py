from django.conf.urls import patterns, url
from django.views.generic import ListView

from galleries.models import Image

urlpatterns = patterns('',
        url(r'^$',
            ListView.as_view(model=Image,),
            name='images',
            ),
        )
