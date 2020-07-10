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
    message.widget.attrs.update({ 'class': 'u-full-width height-p' })
    phone.widget.attrs.update({ 'class': 'u-full-width' })
    company.widget.attrs.update({ 'class': 'u-full-width' })
    email.widget.attrs.update({ 'class': 'u-full-width' })
    lastName.widget.attrs.update({ 'class': 'u-full-width' })
    firstName.widget.attrs.update({ 'class': 'u-full-width' })
