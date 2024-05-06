from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('home/', home, name='home'),
    path('agregar_entrada/', agregar_entrada, name='agregar_entrada'),
    path('configuracion_contraseñas/', configuracion_contraseñas, name='configuracion_contraseñas'),
    path('register/', register, name='register'),
    path('', loginView, name='login'),
    path('logout/', logoutView, name='logout'),

]
