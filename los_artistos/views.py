from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.urls import reverse
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # email = form.cleaned_data['email']
            # message = form.cleaned_data['message']
            # send_mail('LTK - Message', message, email, ['admin@admin.fr'])
            subject = 'Subject'
            data = {'email': form.cleaned_data['email'], 'lastname': form.cleaned_data['lastName'], 'firstname': form.cleaned_data['firstName'], 'company': form.cleaned_data['company'], 'phone': form.cleaned_data['phone'], 'message': form.cleaned_data['message']}
            html_message = render_to_string('./mails/contact_mail.html', data)
            plain_message = strip_tags(html_message)
            from_email = 'From <from@example.com>'
            to = 'to@example.com'
            send_mail(subject, plain_message, from_email, [to], html_message=html_message)

            return redirect('/contact/success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})