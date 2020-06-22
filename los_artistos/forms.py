from django import forms

class ContactForm(forms.Form):
    firstName = forms.CharField(
        required=True
    )
    lastName = forms.CharField(
        required=True
    )
    email = forms.EmailField(
        required=True
    )
    company = forms.CharField(
        required=True
    )
    phone = forms.CharField(
        required=True
    )
    message = forms.CharField(
        widget=forms.Textarea,
        required=True
    )