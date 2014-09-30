from django.contrib import admin

from blog.models import Post
from blog.forms import TagForm


class PostAdmin(admin.ModelAdmin):
    # Changeform page
    fields = ('title', 'status', 'tags', 'text')
    radio_fields = {'status': admin.HORIZONTAL}
#    change_form_template = 'blog/admin/change_form.html'
    form = TagForm

    # Changelist page
    change_list_template = 'admin/change_list_filter_sidebar.html'
    change_list_filter_template = 'admin/filter_listing.html'

    def tags(obj):
        return ', '.join(list(obj.tags.names()))

    list_display = ('title', tags,
                    'status', 'date_created')
    list_filter = ['tags', 'status']
    search_fields = ['title', 'text']

    class Media:
        js = (
            'js/featuredimage.js',
            )

admin.site.register(Post, PostAdmin)
