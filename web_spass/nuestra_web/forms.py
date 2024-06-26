from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import make_password, check_password


class RegisterForm(UserCreationForm):
    username = forms.CharField(label="Nom d'usuari", required=True)
    email = forms.EmailField(label="Correu electronic", required=True)
    password1 = forms.CharField(label="Contrasenya", widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label="Confirmar contrasenya", widget=forms.PasswordInput, required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Registrarse', css_class='btn btn-success'))

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
    

class LoginForm(forms.Form):
    username = forms.CharField(label="Nom d'usuari")
    password = forms.CharField(label="Contrasenya", widget=forms.PasswordInput)

class TwoFactorForm(forms.Form):
    code = forms.CharField(label="Código d'autentificació")
