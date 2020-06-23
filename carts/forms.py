from django import forms
from rates.models import Rate

class CartAddArtworkForm(forms.Form):

    nb_month = forms.ModelChoiceField(
        queryset=Rate.objects.all().order_by('duration')
    )

class CartEmailForm(forms.Form):

    email = forms.EmailField(
        label = "Adresse Email",
        max_length=256,
        required=True,
    )