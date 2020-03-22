from django import forms

from .models import Artwork

class ArtworkForm(forms.ModelForm):

    class Meta:
        model = Artwork
        fields = ('name', 'height','width', 'artist', 'photo')