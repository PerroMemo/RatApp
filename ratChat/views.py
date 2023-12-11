from email import message
from django.shortcuts import render, redirect
from . forms import SignUpForm
from . models import RatRoom, RatMessages, RatSticker

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def index(request):
    return render(request, 'index.html')

def signup(request):
        
    if request.method == 'POST':
  
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('/')
    else:
        form = SignUpForm()
    
    return render(request, 'signup.html', {'form': form})
            

@login_required
def rooms(request):
    rooms = RatRoom.objects.all()

    return render(request, 'rooms.html', {'rooms':rooms})

@login_required
def room(request,slug):
    room = RatRoom.objects.get(slug=slug)
    stickers = RatSticker.objects.all()
    rutas = []

    for i in stickers:
        rutas.append(procesar_ruta(str(i.rat)))
    print(rutas)

    try:
        messages = RatMessages.objects.filter(room=room)  # Ajusta según tu consulta
    except ObjectDoesNotExist:
        # Manejo de la excepción, por ejemplo, redireccionar o devolver un valor predeterminado
        print("No hay mensajes todavia")
    return render(request, 'room.html', {'room':room , 'messages':messages, 'stickers' : stickers})


def procesar_ruta(ruta):
    if ruta.startswith('static/'):
        return ruta[len('static/'):]

    return ruta