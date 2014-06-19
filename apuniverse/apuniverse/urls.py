from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView, ListView

from blog.models import Post

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Homepage
    url(r'^$',
        TemplateView.as_view(template_name='home.html'),
        name='home'),

    # What's new
    url(r'^new/$',
        TemplateView.as_view(template_name='new.html'),
        name='new'),

    # Blog
    # App
    url(r'^blog/',
        include('blog.urls'),
        ),

    # Galleries
    # App
    url(r'^galleries/$',
        TemplateView.as_view(template_name='galleries.html'),
        name='galleries'),

    # About
    url(r'^about/$',
        TemplateView.as_view(template_name='about.html'),
        name='about'),

    # Contact
    # Form
    url(r'^contact/$',
        TemplateView.as_view(template_name='contact.html'),
        name='contact'),

    # Admin
    # App
    url(r'^admin/',
        include(admin.site.urls)),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

)

# Uncomment the next line to serve media files in dev.
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
                            url(r'^__debug__/', include(debug_toolbar.urls)),
                            )
