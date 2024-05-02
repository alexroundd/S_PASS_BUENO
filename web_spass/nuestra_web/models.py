from django.db import models
from django.contrib.auth.models import User
from cryptography.fernet import Fernet
from django.conf import settings
from django.contrib.auth.models import AbstractUser


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
    


class Folder(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, related_name='items')

    def __str__(self):
        return self.name
    