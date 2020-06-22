from django import forms

from .models import Artwork, Artwork_Style

class ArtworkForm(forms.ModelForm):

    class Meta:
        model = Artwork
        fields = ('name', 'height','width', 'artist', 'photo', 'price', 'style')

class ModifyArtworkForm(forms.ModelForm):

    class Meta:
        model = Artwork
        fields = ('name', 'height','width', 'artist', 'photo', 'price', 'style')

class StyleForm(forms.ModelForm):

    class Meta:
        model = Artwork_Style
        fields = ('name', )