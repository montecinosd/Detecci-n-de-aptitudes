from django.shortcuts import render
# from Registro_fullpega.models import *
# from Registro_fullpega.forms import *
from Publicar_trabajo.models import *
from Publicar_trabajo.forms import *

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='/auth/login')
def publicar_trabajo(request):
    data = {}

    #data['form'] = TrabajoForm()
    data["Areas"] = Areas.objects.all()
    aptitudes = Aptitudes.objects.all()
    data['Aptitudes'] = aptitudes

    return render(request, 'publicar_trabajo.html', data)

@login_required(login_url='/auth/login')
def validar_aptitud(request,pk_aptitud):

    data = {}
    usuario = Persona.objects.get(Usuario=3)

    preguntas = Pregunta.objects.filter(Aptitud_vinculada=pk_aptitud)
    data['preguntas'] = preguntas
    if request.method == 'GET':
        print("get")
    else:
        return redirect('validar_aptitud')
    return render(request, 'validar_aptitud.html', data)


@login_required(login_url='/auth/login')
def visualizar_perfil(request,pk_user):
    data = {}
    usuario = Persona.objects.get(Usuario=pk_user)
    data['usuario'] = usuario
    if request.method == 'GET':
        print("get")
    else:
        return redirect('visualizar_perfil')

    return render(request, 'visualizar_perfil.html', data)