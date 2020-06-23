from django import forms

from .models import Artwork, Artwork_Style, Artwork_Category

class ArtworkForm(forms.ModelForm):

    class Meta:
        model = Artwork
        fields = ('name', 'height','width', 'artist', 'photo', 'price', 'style', 'category')

class ModifyArtworkForm(forms.ModelForm):

    class Meta:
        model = Artwork
        fields = ('name', 'height','width', 'artist', 'photo', 'price', 'style', 'category')

class StyleForm(forms.ModelForm):

    class Meta:
        model = Artwork_Style
        fields = ('name', )

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Artwork_Category
        fields = ('name', )