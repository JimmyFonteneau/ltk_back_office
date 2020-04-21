from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.urls import reverse

from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            send_mail('LTK - Message', message, email, ['admin@admin.fr'])
            return redirect('/contact/success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})