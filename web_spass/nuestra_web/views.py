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
    if not request.user.is_authenticated:
        return redirect('/')

    grupos = Grupo.objects.filter(propietario=request.user.id)
    contenidos = Contenido.objects.filter(propietario=request.user.id)

    context = {
          'grupos': grupos, 
          'contenidos': contenidos,
    }
    return render(request, 'home.html',context=context)

def configuracion_contraseñas(request):
    return render(request, 'configuracion_contraseñas.html')

def logoutView(request):
    logout(request) 
    return redirect('login')  # Redirige a la página de inicio de sesión después de cerrar sesión

def crear_grupo(request):
    if not request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST':
        titulo = request.POST['titulo']
        Grupo.objects.create(titulo=titulo,propietario=request.user)
        return redirect('home')
    
    return render(request, 'crear_grupo.html')

def eliminar_grupo(request, grupo_id):
    grupo = Grupo.objects.get(id=grupo_id)
    grupo.delete()
    return redirect('home')

def grupo_contentadduser(request):
    if not request.user.is_authenticated:
        return redirect('/')
    
    grupos = Grupo.objects.filter(propietario=request.user.id)
    contenidos = Contenido.objects.filter(propietario=request.user.id)

    if request.method == 'POST':
        grupos_POST_VALUE = request.POST.get('grupos', '')
        contenido_POST_VALUE = request.POST.getlist('contenido', '')

        print(grupos_POST_VALUE,contenido_POST_VALUE)

        post_group_query = Grupo.objects.get(id=grupos_POST_VALUE)
        for contenido in contenido_POST_VALUE:
            post_group_query.contenido_del_grupo.add(contenido)
        return redirect('/')

    else:
        return render(request, 'agregar_grupo.html', {'grupos': grupos, 'contenidos': contenidos})

def grupo_detalle(request, grupo_id):
    grupo = get_object_or_404(Grupo, id=grupo_id)
    grupos = Grupo.objects.all()
    
    return render(request, 'grupo_detalle.html', {'grupo': grupo, 'grupos': grupos})

def agregar_contenido(request):
    form = ContenidoForm()
    if not request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST':
        form = ContenidoForm(request.POST)
        titulo_POST_VALUE = request.POST.get('titulo', '')
        username_POST_VALUE = request.POST.get('username', '')
        contraseña_POST_VALUE = request.POST.get('contraseña', '')
        contraseña_confirmacion_POST_VALUE = request.POST.get('contraseña_confirmacion', '')
        link_POST_VALUE = request.POST.get('link', '')
        
        if form.is_valid():            
            Contenido.objects.create(propietario=request.user,titulo=titulo_POST_VALUE,username=username_POST_VALUE,contraseña=contraseña_POST_VALUE,link=link_POST_VALUE).save()
            
            return redirect('home')  
        else:
            if contraseña_POST_VALUE != contraseña_confirmacion_POST_VALUE:
                return render(request, 'agregar_contenido.html', {'form': form, 'error': 'Las contraseñas no coinciden'}) 
            else:
                return render(request, 'agregar_contenido.html', {'form': form, 'error': 'Algo en el servidor a fallado, vuelve a intentarlo mas tarde.'}) 

    else:
        return render(request, 'agregar_contenido.html', {'form': form}) 
    
def editar_contenido(request, contenido_id):
    contenido = get_object_or_404(Contenido, id=contenido_id)
    if request.method == 'POST':
        form = ContenidoForm(request.POST, instance=contenido)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            # Handle form validation errors
            messages.error(request, 'Error al guardar los cambios')
    else:
        form = ContenidoForm(instance=contenido)
    return render(request, 'editar_contenido.html', {'form': form})
    
def eliminar_elemento(request, contenido_id):
    if request.method == 'POST':
        item = Contenido.objects.get(pk=contenido_id)
        item.delete()
    return redirect('home')

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