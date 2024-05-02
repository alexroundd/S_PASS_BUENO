from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', home, name='home'),
    path('agregar_entrada/', agregar_entrada, name='agregar_entrada'),
    path('configuracion_contraseñas/', directory_manager, name='configuracion_contraseñas'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),

]
