from django import forms

from .models import UserProfile


class RegisterForm(forms.Form):

    email = forms.EmailField(
        label = "Adresse Email",
        max_length=256,
        required=True,
    )
    raw_password = forms.CharField(
        label = "Mot de passe",
        max_length=256,
        min_length=10,
        required=True,
        help_text = "10 caractères minimum",
        widget=forms.PasswordInput(),
    )
    raw_password_confirmation = forms.CharField(
        label = "Mot de passe (confirmation)",
        max_length=256,
        min_length=10,
        required=True,
        widget=forms.PasswordInput(),
    )
    firstname = forms.CharField(
        label = "Prénom",
        max_length=256,
        required=True,
    )
    lastname = forms.CharField(
        label = "Nom de famille",
        max_length=256,
        required=True,
    )
    company = forms.CharField(
        label = "Entreprise",
        max_length=256,
        required=False,
    )
    phone = forms.CharField(
        label = "Téléphone",
        max_length=12,
        required=False,
    )
    
    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        raw_password = cleaned_data.get('raw_password')
        raw_password_confirmation = cleaned_data.get('raw_password_confirmation')
        if len(raw_password) < 10:
            raise forms.ValidationError("Le mot de passe doit faire 10 caractères minimum")
        if raw_password and raw_password_confirmation:
            if raw_password != raw_password_confirmation:
                raise forms.ValidationError("Les mots de passe ne sont pas identiques")
        
        try:
            UserProfile.objects.get(email=cleaned_data['email'])
        except UserProfile.DoesNotExist:
            pass
        else:
            raise forms.ValidationError("Cet utilisateur existe déjà")

        return cleaned_data
        

class LoginForm(forms.Form):

    email = forms.CharField(
        label = "Email",
        max_length=64,
        required=True,
    )
    password = forms.CharField(
        label = "Mot de passe",
        max_length=256,
        required=True,
        widget=forms.PasswordInput(),
    )


class AccountSettingsForm(forms.ModelForm):
  
    class Meta:
        model = UserProfile
        fields = ('firstname', 'lastname')