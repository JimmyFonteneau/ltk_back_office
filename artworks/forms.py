from django import forms

from .models import Artwork, Artwork_Style, Artwork_Category, Artwork_Storage_Place

class ArtworkForm(forms.ModelForm):

    class Meta:
        model = Artwork
        fields = ('name', 'height','width', 'artist', 'photo', 'price', 'style', 'category', 'storage_place', 'state', 'description', 'introduction')

class ModifyArtworkForm(forms.ModelForm):

    class Meta:
        model = Artwork
        fields = ('name', 'height','width', 'artist', 'photo', 'price', 'style', 'category', 'storage_place', 'state', 'spotlight', 'timer', 'description', 'introduction')
        widgets = {
            'timer': forms.DateInput(
                attrs={'type': 'date'},
                format='%Y-%m-%d'
            )
        }

class StyleForm(forms.ModelForm):

    class Meta:
        model = Artwork_Style
        fields = ('name', )

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Artwork_Category
        fields = ('name', )

class StoragePlaceForm(forms.ModelForm):

    class Meta:
        model = Artwork_Storage_Place
        fields = ('name', )