from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
import os
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import PasswordOptionsForm
import string
import random
from django.http import JsonResponse


def register(request):
#    if request.user.is_authenticated:
#        return redirect('login')  # Redirige a la página principal si ya está autenticado
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def loginView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home') 
            else:
                messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def home(request):
    grupos = Grupo.objects.all()
    contenidos = Contenido.objects.all()

    return render(request, 'home.html', {'grupos': grupos, 'contenidos': contenidos})

def agregar_entrada(request):
    if request.method == 'POST':
        form = EntradaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'La entrada se ha agregado correctamente.')
            return redirect('home')
        else:
            messages.error(request, 'Ha ocurrido un error al guardar la entrada. Por favor, revisa los datos e inténtalo de nuevo.')
    else:
        form = EntradaForm()
    return render(request, 'agregar_entrada.html', {'form': form})

def configuracion_contraseñas(request):
    return render(request, 'configuracion_contraseñas.html')

def my_view(request):
    if request.user.is_authenticated:
        # El usuario está autenticado, realiza las acciones necesarias
        # Por ejemplo, muestra un mensaje de bienvenida, etc.
        return render(request, 'loggedin.html')
    else:
        # El usuario no está autenticado, realiza acciones alternativas
        return render(request, 'notloggedin.html')

def logoutView(request):
    logout(request) 
    return redirect('login')  # Redirige a la página de inicio de sesión después de cerrar sesión

def grupos(request):
    grupos = Grupo.objects.all()
    return render(request, 'home.html', {'grupos': grupos})

def crear_grupo(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        Grupo.objects.create(titulo=titulo)
        return redirect('home')
    return render(request, 'crear_grupo.html')

def eliminar_grupo(request, grupo_id):
    grupo = Grupo.objects.get(id=grupo_id)
    grupo.delete()
    return redirect('home')

def grupo_detalle(request, grupo_id):
    grupo = get_object_or_404(Grupo, id=grupo_id)
    contenidos = Contenido.objects.all()

    return render(request, 'grupo_detalle.html', {'grupo': grupo, 'contenidos': contenidos})

def agregar_contenido(request):
    if request.method == 'POST':
        form = ContenidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Reemplaza 'nombre_de_la_vista_que_muestra_el_contenido' con el nombre real de tu vista
    else:
        form = ContenidoForm()
    return render(request, 'agregar_contenido.html', {'form': form})  # Reemplaza 'nombre_de_la_plantilla.html' con el nombre real de tu plantilla

def contenido(request):
    contenidos = Contenido.objects.all()
    return render(request, 'contenido.html', {'contenidos': contenidos})

def generar_contraseña(length, uppercase, lowercase, numbers, special):
    characters = ''
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if numbers:
        characters += string.digits
    if special:
        characters += string.punctuation

    return ''.join(random.choice(characters) for _ in range(length))

def generador(request):
    if request.method == 'POST':
        form = PasswordOptionsForm(request.POST)
        if form.is_valid():
            password = generar_contraseña(
                length=form.cleaned_data['length'],
                uppercase=form.cleaned_data['uppercase'],
                lowercase=form.cleaned_data['lowercase'],
                numbers=form.cleaned_data['numbers'],
                special=form.cleaned_data['special']
            )
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                            return JsonResponse({'password': password})
            else:
                            # Para solicitudes no AJAX, puedes decidir qué hacer,
                            # por ejemplo, redirigir o manejar de otra manera.
                            return render(request, 'password_result.html', {'password': password})
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                            return JsonResponse({'error': 'Formulario inválido.'}, status=400)
            else:
                            # Manejar errores de formulario para solicitudes no AJAX
                            return render(request, 'password_form.html', {'form': form})
    else:
                    form = PasswordOptionsForm()
                    return render(request, 'password_form.html', {'form': form})