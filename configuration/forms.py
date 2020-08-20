from django import forms

from .models import Configuration

class ModifyConfiguration(forms.ModelForm):

    class Meta:
        model = Configuration
        fields = ('email',)