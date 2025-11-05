from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import IntegrityError
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import FormularioServicio
from .models import Servicio
from django.contrib import messages
from Reserva.models import Reserva

# Create your views here.

def inicio_admin(request):
    servicios = Servicio.objects.all()[:6]
    return render(request, 'inicio_admin.html',{
        'servicios' : servicios
    })


def registrar_admin(request):
    if request.method == 'POST':
        try:
            if request.POST['password1'] == request.POST['password2']:
                usuario = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1']
                )
                admin_group = Group.objects.get(name='administrador')  # Asume que el grupo existe
                usuario.groups.add(admin_group)
                usuario.save()
                messages.success(request, 'Administrador registrado correctamente.')
                return render(request, 'registro_admin.html', {
        'form': UserCreationForm(),
    })
            else:
                messages.error(request, 'Las contraseñas no coinciden.')
        except IntegrityError:
            messages.error(request, 'El usuario ya existe.')
    
    return render(request, 'registro_admin.html', {
        'form': UserCreationForm(),
    })

def crear_servicio(request):
    if request.method == 'POST':
        form = FormularioServicio(request.POST, request.FILES)
        if form.is_valid():
            servicio = form.save(commit=False)
            servicio.save()
            messages.success(request, 'Servicio creado correctamente.')
            return render(request, 'crear_servicio.html', {
        'form': FormularioServicio(),
    })
        else:
            messages.error(request, 'Hubo un error al crear el servicio.')

    return render(request, 'crear_servicio.html', {
        'form': FormularioServicio(),
    })

def ver_servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'ver_servicios.html',{
        'servicios' : servicios
    })

def servicio_detalle(request, id):
    servicio = get_object_or_404(Servicio, pk=id)
    return render(request, 'servicio_detalle.html',{
        'servicio' : servicio
    })

def actualizar_servicio(request, id):
    servicio = get_object_or_404(Servicio, pk=id)
    if request.method == 'POST':
        form = FormularioServicio(request.POST, request.FILES, instance=servicio)
        if form.is_valid():
            form.save()
            return redirect('ver_servicios')
        else:
            return render(request, 'crear_servicio.html', {'form': form})

    return render(request, 'crear_servicio.html',{
        'form' : FormularioServicio(instance=servicio)
    })


def eliminar_servicio(request, id):
    servicio = get_object_or_404(Servicio, pk=id)
    if request.method == 'POST':
        servicio.delete()
    return redirect('ver_servicios')


def ver_reservas(request):
    reservas = Reserva.objects.all()
    return render(request, 'ver_reservas.html', {
        'reservas': reservas
    })