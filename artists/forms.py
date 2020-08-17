from django import forms

from .models import Artist

class ArtistForm(forms.ModelForm):

    class Meta:
        model = Artist
        fields = ('firstname', 'lastname','name', 'artist_description', 'artist_universe','photo')

class ModifyArtistForm(forms.ModelForm):

    class Meta:
        model = Artist
        fields = ('firstname', 'lastname','name', 'spotlight', 'artist_description', 'artist_universe','photo')
