from django import forms

class ContactForm(forms.Form):
    firstName = forms.CharField(
        label="Prénom",
        max_length=256,
        required=True
    )
    lastName = forms.CharField(
        label="Nom",
        max_length=256,
        required=True
    )
    email = forms.EmailField(
        label="Email",
        max_length=256,
        required=True
    )
    company = forms.CharField(
        label="Entreprise",
        max_length=256,
        required=True
    )
    phone = forms.CharField(
        label="Numéro de Télephone",
        max_length=256,
        required=True
    )
    message = forms.CharField(
        widget=forms.Textarea,
        max_length=500,
        required=True
    )
    message.widget.attrs.update({ 'class': 'u-full-width height-p' })
    phone.widget.attrs.update({ 'class': 'u-full-width' })
    company.widget.attrs.update({ 'class': 'u-full-width' })
    email.widget.attrs.update({ 'class': 'u-full-width' })
    lastName.widget.attrs.update({ 'class': 'u-full-width' })
    firstName.widget.attrs.update({ 'class': 'u-full-width' })
