from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.forms import AuthenticationForm

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




    