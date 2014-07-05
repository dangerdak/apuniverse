from django.contrib import admin

from blog.models import Post
from blog.forms import TagForm


class PostAdmin(admin.ModelAdmin):
    # Changeform page
    exclude = ('slug',)
    change_form_template = 'blog/admin/change_form.html'
    form = TagForm

    # Changelist page
    list_display = ('title', 'tag_names',
                    'is_published', 'date_created')
    list_filter = ['tags']
    search_fields = ['title', 'text']

admin.site.register(Post, PostAdmin)
