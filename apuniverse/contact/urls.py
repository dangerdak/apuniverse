from django.conf.urls import patterns, url
from django.views.generic import TemplateView


urlpatterns = patterns('',
        # Form
        url(r'^$',
            'contact.views.contact',
            name='contact_form'),

        url(r'^thanks/$',
            TemplateView.as_view(template_name='contact/thanks.html'),
            name='contact_thanks'),
)
