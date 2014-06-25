from django.contrib import admin

from image_cropping import ImageCroppingMixin
from galleries.models import Gallery, Image


#class GalleryAdmin(admin.ModelAdmin):
#    list_display = ['title', 'slug', 'project_year', 'image', 'blog_link', 'summary']

class ImageAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass

admin.site.register(Gallery)
admin.site.register(Image, ImageAdmin)
