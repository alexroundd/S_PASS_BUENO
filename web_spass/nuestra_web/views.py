from django.shortcuts import render, redirect 
from .models import *
from .forms import EntradaForm
import os
from django.http import JsonResponse
from .forms import FolderForm, ItemForm
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from django.contrib.auth import login as auth_login

def register(request):
#    if request.user.is_authenticated:
#        return redirect('login')  # Redirige a la página principal si ya está autenticado
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Inicia sesión automáticamente al usuario registrado
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def loginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('home')  # Redirige a la página de inicio después del inicio de sesión
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def home(request):
    entradas = Entrada.objects.all()[:3]
    return render(request, 'home.html', {'entradas': entradas})


def agregar_entrada(request):
    if request.method == 'POST':
        form = EntradaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EntradaForm()
    return render(request, 'agregar_entrada.html', {'form': form})


def configuracion_contraseñas(request):
    return render(request, 'configuracion_contraseñas.html')



def directory_manager(request):
    if request.method == 'POST':
        if 'folder_name' in request.POST:
            folder_form = FolderForm(request.POST)
            if folder_form.is_valid():
                folder = folder_form.save(commit=False)
                folder.owner = request.user
                folder.save()
        elif 'item_name' in request.POST:
            item_form = ItemForm(request.POST)
            if item_form.is_valid():
                item = item_form.save(commit=False)
                item.folder_id = request.POST.get('folder_id')
                item.save()
                
    folders = Folder.objects.filter(owner=request.user)
    return render(request, 'configuracion_contraseñas.html', {
        'folders': folders,
        'folder_form': FolderForm(),
        'item_form': ItemForm(),
    })