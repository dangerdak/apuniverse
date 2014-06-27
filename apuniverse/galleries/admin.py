from django.contrib import admin

from image_cropping import ImageCroppingMixin
from galleries.models import Gallery, Image


class ImageInline(ImageCroppingMixin, admin.StackedInline):
    model = Image
    max_num = 16
    template = 'galleries/admin/stacked.html'
    extra = 1
    fieldsets = [
        (None,  {'fields': ['title', 'image', 'thumbnail']}),
        ('Detailed Info',  {'fields': ['date', 'medium', 'size'], 'classes': ['collapse']}),
        ('Advanced',    {'fields': ['slug'], 'classes': ['collapse']}),
    ]
    prepopulated_fields = {"slug": ("title",)}


class GalleryAdmin(admin.ModelAdmin):
    inlines = [ImageInline]

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            '/static/galleries/jquery.sortable.js'
        )
        css = {
            'all': ('/static/galleries/stacked-inline.css',
                    '/static/galleries/sortable.css',)
        }


class ImageAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ('title', 'gallery', 'thumbnail')

admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Image, ImageAdmin)
