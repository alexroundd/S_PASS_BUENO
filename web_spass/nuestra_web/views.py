from django.shortcuts import render, redirect 
from .models import *
from .forms import EntradaForm

# Create your views here.

def home(request):
    # Obtén todas las instancias de Entrada
    entradas = Entrada.objects.all()[:3]
    # Renderiza la plantilla con las entradas en el contexto
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