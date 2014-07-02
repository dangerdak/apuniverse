from django.contrib import admin

from blog.models import Post
from blog.forms import TagForm


class PostAdmin(admin.ModelAdmin):
    change_form_template = 'blog/admin/change_form.html'
    prepopulated_fields = {"slug": ("title",)}

    form = TagForm

admin.site.register(Post, PostAdmin)
