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

    path('grupos/', grupos, name='grupos'),
    path('crear_grupo/', crear_grupo, name='crear_grupo'),
    path('eliminar_grupo/<int:grupo_id>/', eliminar_grupo, name='eliminar_grupo'),
    path('grupo/<int:grupo_id>/', grupo_detalle, name='grupo_detalle'),

    path('agregar_contenido/', agregar_contenido, name='agregar_contenido'),
    path('contenido/', contenido, name='contenido'),

    path('generador/', generador, name='generador'),

]
