from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('agregar_entrada/', agregar_entrada, name='agregar_entrada'),
    path('configuracion_contraseñas/', configuracion_contraseñas, name='configuracion_contraseñas'),

]
