from django import forms
from rates.models import Rate

class CartAddArtworkForm(forms.Form):

    nb_month = forms.ModelChoiceField(
        queryset=Rate.objects.all(),
        initial=Rate.objects.all()
    )