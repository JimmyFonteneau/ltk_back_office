from django import forms

class OrderEmailForm(forms.Form):

    email = forms.EmailField(
        label = "Adresse Email",
        max_length=256,
        required=True,
    )