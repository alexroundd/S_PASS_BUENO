from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import make_password, check_password

class LoginForm(forms.Form):
    username = forms.CharField(label="Nombre de usuario")
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)

class RegisterForm(UserCreationForm):
    username = forms.CharField(label="Nombre de usuario", required=True)
    email = forms.EmailField(label="Correo electrónico", required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput, required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Registrarse', css_class='btn btn-success'))

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
        if contraseña and repetir_contraseña and contraseña != repetir_contraseña:
            raise forms.ValidationError('Las contraseñas no coinciden. Por favor, inténtalo de nuevo.')

        return cleaned_data

class ContenidoForm(forms.ModelForm):
    contraseña_confirmacion = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Contenido
        fields = ['titulo', 'username', 'contraseña', 'contraseña_confirmacion', 'link']
        widgets = {
            'contraseña': forms.PasswordInput,
        }

    def clean(self):
        cleaned_data = super().clean()
        contraseña = cleaned_data.get('contraseña')
        contraseña_confirmacion = cleaned_data.get('contraseña_confirmacion')

        if contraseña != contraseña_confirmacion:
            raise forms.ValidationError("Las contraseñas no coinciden.")
    
class PasswordOptionsForm(forms.Form):
    length = forms.IntegerField(label='Longitud', initial=16, min_value=8, max_value=100)
    uppercase = forms.BooleanField(label='Incluir mayúsculas', required=False, initial=True)
    lowercase = forms.BooleanField(label='Incluir minúsculas', required=False, initial=True)
    numbers = forms.BooleanField(label='Incluir números', required=False, initial=True)
    special = forms.BooleanField(label='Incluir caracteres especiales', required=False, initial=True)