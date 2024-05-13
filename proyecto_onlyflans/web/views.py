from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Flan, ContactForm
from .forms import ContactFormModelForm, LoginForm, PedidoForm, PedidoFormPremium
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def indice(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    return render(request, 'index.html', {'flanes': flanes_publicos})
    
def acerca(request):
    return render(request, 'about.html')

#requiere login para mostrar bienvenido 
@login_required
def bienvenido(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    return render(request, 'welcome.html', {'flanes': flanes_privados})

def contacto(request):
    if request.method == 'POST':
        form = ContactFormModelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/exito_contacto/')
    else:
        form = ContactFormModelForm()
    return render(request, 'contacto.html', {'form': form})

def exito_contacto(request):
    return render(request, 'exito_contacto.html')


def iniciar_sesion(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/bienvenido/')  # Redirige al usuario a la página de bienvenida si las credenciales son válidas
    
        messages.error(request, 'Usuario o contraseña incorrectos') 
    
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def cerrar_sesion(request):
    logout(request)
    # Establecer un mensaje de éxito
    messages.success(request, 'Has cerrado sesión exitosamente. Serás redirigido a la página de inicio.')
    return redirect('/')  # Redirige al usuario a la página de inicio después de cerrar sesión
    
#vista para los pedidos básicos
def hacer_pedido(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pagina_de_confirmacion')
    else:
        form = PedidoForm()
    return render(request, 'hacer_pedido.html', {'form': form, 'flanes': flanes_publicos})

#vista pedidos premium
def hacer_pedido_premium(request):
    if request.method == 'POST':
        form = PedidoFormPremium(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pagina_de_confirmacion')
    else:
        form = PedidoFormPremium()
    return render(request, 'hacer_pedido_premium.html', {'form': form})

def pagina_de_confirmacion(request):
    return render(request, 'pagina_de_confirmacion.html')


