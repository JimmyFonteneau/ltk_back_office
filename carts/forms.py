from django import forms

ARTWORK_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 10)]

class CartAddArtworkForm(forms.Form):

    quantity = forms.TypedChoiceField(
        choices=ARTWORK_QUANTITY_CHOICES,
        coerce=int,
        label="Quantité"
    )
    
    update = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput
    )