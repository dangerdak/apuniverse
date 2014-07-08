from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import EmailMessage, BadHeaderError
from django.core.exceptions import SuspiciousOperation

from contact.forms import ContactForm


def contact(request):
    # If the form has been submitted...
    if request.method == 'POST':
        # Bound form
        form = ContactForm(request.POST)
        if form.is_valid():
            no_fill = form.cleaned_data['no_fill']
            # Don't send email if honeypot is filled in
            # but redirect anyway
            if (no_fill):
                return HttpResponseRedirect('/contact/thanks/')

            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender_email = form.cleaned_data['sender_email']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ['annie.potter@email.com']
            if cc_myself:
                recipients.append(sender_email)

            email = EmailMessage(subject, message, sender_email, recipients,
                                 headers={'Reply-To': sender_email})
            try:
                email.send(fail_silently=True)
            # Prevent header injection
            except BadHeaderError:
                raise SuspiciousOperation()

            return HttpResponseRedirect('/contact/thanks/')
    else:
        # Unbound form
        form = ContactForm()

    return render(request, 'contact/form.html', {
        'form': form,
        })
