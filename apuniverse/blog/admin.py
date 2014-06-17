from django.contrib import admin

from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    change_form_template = 'blog/admin/change_form.html'

admin.site.register(Post, PostAdmin)
