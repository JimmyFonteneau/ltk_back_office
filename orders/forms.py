from django import forms
from .models import Order, OrderArtworkRate

class OrderEmailForm(forms.Form):

    email = forms.EmailField(
        label = "Adresse Email",
        max_length=256,
        required=True,
    )

class OrderUpdate(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('price', 'state')

class ReturnDateUpdate(forms.ModelForm):

    class Meta:
        model = OrderArtworkRate
        fields = ('return_date',)