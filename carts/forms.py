from django import forms
from rates.models import Rate

class CartAddArtworkForm(forms.Form):

    nb_month = forms.ModelChoiceField(
<<<<<<< HEAD
        queryset=Rate.objects.all().order_by('duration')
=======
        queryset=Rate.objects.all(),
        initial=Rate.objects.all()
>>>>>>> 0b6e6c02f313771f44a37872b107cc161ea84272
    )