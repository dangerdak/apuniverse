from django import forms


class ContactForm(forms.Form):
    sender_email = forms.EmailField(label='Your Email Address')
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    cc_myself = forms.BooleanField(required=False)
    # Honeypot
    no_fill = forms.CharField(label='', required=False)

    class Media:
        css = {
            'all': ('/static/css/contact.css',)
        }
