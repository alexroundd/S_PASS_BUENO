from django.db import models
from django.contrib.auth.models import User
from cryptography.fernet import Fernet
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from cryptography.fernet import Fernet
from django.core.validators import MinLengthValidator

# Create your models here.




def encriptar_contraseñas(contraseña):
    cifrador = Fernet(settings.CLAVE_ENCRIPTACION)
    return cifrador.encrypt(contraseña.encode()).decode()

def desencriptar_contraseña(contraseña_encriptada):
    cifrador = Fernet(settings.CLAVE_ENCRIPTACION)
    return cifrador.decrypt(contraseña_encriptada.encode()).decode()

class Entrada(models.Model):
    titulo = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    contraseña_encriptada = models.CharField(max_length=255)  # Se almacenará la contraseña encriptada
    calidad = models.CharField(max_length=50)
    url = models.URLField(max_length=200)
    
    def __str__(self):
        return self.titulo
    
    def save(self, *args, **kwargs):
        # Antes de guardar, encriptar la contraseña
        self.contraseña_encriptada = encriptar_contraseñas(self.contraseña_encriptada)
        super().save(*args, **kwargs)
    
    def obtener_contraseña(self):
        # Al obtener la contraseña, desencriptarla
        return desencriptar_contraseña(self.contraseña_encriptada)
    
class Grupo(models.Model):
    titulo = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo
    

class Contenido(models.Model):
    TITULO_CHOICES = [
        ('Baja', 'Baja'),
        ('Media', 'Media'),
        ('Alta', 'Alta'),
        ('Muy Alta', 'Muy Alta'),
    ]
    titulo = models.CharField(max_length=100)
    username = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=100, default='', validators=[MinLengthValidator(8)])
    calidad_contraseña = models.CharField(max_length=10, choices=TITULO_CHOICES, default='Baja')
    link = models.CharField(max_length=200, null=True) # Puedes cambiar el tipo de campo si necesitas algo más específico

    def __str__(self):
        return self.titulo
    
    
    def calcular_calidad_contraseña(self):
        longitud = len(self.contraseña)
        caracteres_especiales = any(char.isalnum() for char in self.contraseña)
        tiene_minusculas = any(char.islower() for char in self.contraseña)
        tiene_mayusculas = any(char.isupper() for char in self.contraseña)

        if longitud >= 8 and caracteres_especiales and tiene_minusculas and tiene_mayusculas:
            if longitud >= 16:
                self.calidad_contraseña = 'Muy Alta'
            else:
                self.calidad_contraseña = 'Alta'
        elif longitud >= 8:
            self.calidad_contraseña = 'Media'
        else:
            self.calidad_contraseña = 'Baja'

    def save(self, *args, **kwargs):
        self.calcular_calidad_contraseña()
        super(Contenido, self).save(*args, **kwargs)


