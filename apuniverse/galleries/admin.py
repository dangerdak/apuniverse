from django.contrib import admin
from django.db.models import Count

from image_cropping import ImageCroppingMixin

from galleries.forms import TagForm
from galleries.models import Gallery, Image


class ImageInline(ImageCroppingMixin, admin.StackedInline):
    model = Image
    fieldsets = [
        (None,  {'fields': ['title', 'image', 'thumbnail']}),
        ('Detailed Info',  {'fields': ['date', 'medium', 'size'],
                            'classes': ['grp-collapse grp-closed']}),
        ('Advanced',    {'fields': ['thumbnail_position'],
                         'classes': ['grp-collapse grp-closed']}),
    ]
    readonly_fields = ['thumbnail_url']
    extra = 0
    classes = ['grp-collapse grp-open']


class GalleryAdmin(admin.ModelAdmin):
    # Changeform page
    inlines = [ImageInline]
    fields = ['title', 'status', 'project_year', 'linked_blog',
              'summary', 'tags']
    radio_fields = {'status': admin.HORIZONTAL}
    form = TagForm

    def get_form(self, request, obj=None, **kwargs):
        form = super(GalleryAdmin, self).get_form(request, obj, **kwargs)
        blog_link = form.base_fields['linked_blog']
        blog_link.widget.can_add_related = False
        return form

    # Changelist page
    change_list_template = 'admin/change_list_filter_sidebar.html'
    change_list_filter_template = 'admin/filter_listing.html'

    def queryset(self, request):
        return Gallery.objects.annotate(Count('image'))

    def image_count(self, obj):
        return obj.image__count
    image_count.admin_order_field = 'image__count'
    image_count.short_description = 'Number of images'

    def tags(obj):
        return ', '.join(list(obj.tags.names()))

    list_display = ('title', tags, 'status', 'project_year', 'image_count',
                    'blog_url', 'date_created')
    list_filter = ['tags', 'project_year']
    search_fields = ['title', 'summary']

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'galleries/jquery.sortable.js',
            'js/stacked.js',
        )
        css = {
            'all': ('/static/galleries/sortable.css',)
        }


class ImageAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ('title', 'gallery', 'thumbnail_url')

admin.site.register(Gallery, GalleryAdmin)
