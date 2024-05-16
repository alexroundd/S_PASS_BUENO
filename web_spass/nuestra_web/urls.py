from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', home, name='home'),
    path('configuracion_contraseñas/', configuracion_contraseñas, name='configuracion_contraseñas'),
    path('register/', register, name='register'),
    path('logout/', logoutView, name='logout'),
    path('crear_grupo/', crear_grupo, name='crear_grupo'),
    path('eliminar_grupo/<int:grupo_id>/', eliminar_grupo, name='eliminar_grupo'),
    path('grupo/<int:grupo_id>/', grupo_detalle, name='grupo_detalle'),
    path('grupo_contentadduser/', grupo_contentadduser, name='grupo_contentadduser'),
    path('agregar_contenido/', agregar_contenido, name='agregar_contenido'),
    path('generador/', generador, name='generador'),
    path('eliminar/<int:contenido_id>/', eliminar_elemento, name='eliminar_elemento'),
    path('editar_contenido/<int:contenido_id>/', editar_contenido, name='editar_contenido'),
    path('login/', login_view, name='login'),
    path('two_factor/', two_factor_view, name='two_factor'),
    

]

