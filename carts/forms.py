from django import forms

ARTWORK_NB_MONTH_CHOICES = [(1,"3"),(2,"6"),(3,"9")]

class CartAddArtworkForm(forms.Form):

    nb_month = forms.TypedChoiceField(
        choices=ARTWORK_NB_MONTH_CHOICES,
        coerce=int,
        label="Nombre de Mois"
    )
    
    update = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput
    )