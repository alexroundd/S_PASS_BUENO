from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

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


class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ['name', 'parent']  # Incluye 'parent' si deseas permitir folders anidados

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'content', 'folder']  # Asegúrate de manejar el campo 'folder' adecuadamente en la vista