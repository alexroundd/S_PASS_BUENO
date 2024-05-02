from django import forms
from .models import Entrada

class EntradaForm(forms.ModelForm):
    contraseña = forms.CharField(widget=forms.PasswordInput(), label='Contraseña')
    repetir_contraseña = forms.CharField(widget=forms.PasswordInput(), label='Repetir Contraseña')

    class Meta:
        model = Entrada
        fields = ['titulo', 'username', 'contraseña', 'calidad', 'url']

    def clean(self):
        cleaned_data = super().clean()
        contraseña = cleaned_data.get('contraseña')
        repetir_contraseña = cleaned_data.get('repetir_contraseña')

        # Verificar que las contraseñas coincidan
        if contraseña != repetir_contraseña:
            raise forms.ValidationError('Las contraseñas no coinciden. Por favor, inténtalo de nuevo.')

        return cleaned_data
