from django import forms


class ContactForm(forms.Form):
    sender_email = forms.EmailField(label='Your Email Address')
    subject = forms.CharField(max_length=100)
    message = forms.CharField()
    cc_myself = forms.BooleanField(required=False)
