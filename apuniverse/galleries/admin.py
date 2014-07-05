from django.contrib import admin

from image_cropping import ImageCroppingMixin

from galleries.forms import TagForm
from galleries.models import Gallery, Image


class ImageInline(ImageCroppingMixin, admin.StackedInline):
    model = Image
    template = 'admin/edit_inline/stacked.html'
    fieldsets = [
        (None,  {'fields': ['title', 'image', 'thumbnail']}),
        ('Detailed Info',  {'fields': ['date', 'medium', 'size'], 'classes': ['grp-collapse grp-closed']}),
        ('Advanced',    {'fields': ['thumbnail_position'], 'classes': ['grp-collapse grp-closed']}),
    ]
    readonly_fields = ['thumbnail_url']
    extra = 0
    classes = ['grp-collapse grp-open']
    inline_classes = ['grp-collapse grp-closed']


class GalleryAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    fields = ['title', 'project_year', 'blog_link', 'summary', 'tags']
    form = TagForm

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            '/static/galleries/jquery.sortable.js'
        )
        css = {
            'all': ('/static/galleries/stacked-inline.css',
                    '/static/galleries/sortable.css',)
        }
    save_on_top = True


class ImageAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ('title', 'gallery', 'thumbnail_url')

admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Image, ImageAdmin)
