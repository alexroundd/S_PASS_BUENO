from django.shortcuts import render, redirect 
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
    entradas = Entrada.objects.all()[:5]
    return render(request, 'home.html', {'entradas': entradas})

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

