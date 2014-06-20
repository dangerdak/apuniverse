from django.shortcuts import render
from django.http import HttpResponseRedirect

from contact.forms import ContactForm


def contact(request):
    # If the form has been submitted...
    if request.method == 'POST':
        # Bound form
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender_email = form.cleaned_data['sender_email']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ['anniepotter.site@gmail.com']
            if cc_myself:
                recipients.append(sender_email)

            from django.core.mail import send_mail
            send_mail(subject, message, sender_email, recipients,
                      fail_silently=False)
            return HttpResponseRedirect('/contact/thanks/')
    else:
        # Unbound form
        form = ContactForm()

    return render(request, 'contact/form.html', {
        'form': form,
        })
