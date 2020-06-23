from django import forms

from .models import Artist

class ArtistForm(forms.ModelForm):

    class Meta:
        model = Artist
        fields = ('firstname', 'lastname','name',)

class ModifyArtistForm(forms.ModelForm):

    class Meta:
        model = Artist
        fields = ('firstname', 'lastname','name', 'spotlight',)
