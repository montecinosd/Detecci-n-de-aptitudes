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
    usuario = Persona.objects.get(Usuario=request.user.pk)

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
    data['aptidudes_validadas'] = Aptitude_validadas.objects.filter(Usuario=pk_user)
    portafolio=[]
    for i in data['aptidudes_validadas']:
        print("en for")
        print(i.Aptitud_validada.pk)
        portafolio_aptitud= Portafolio.objects.filter(aptitude_validadas = i.Aptitud_validada.pk)
        print(portafolio_aptitud)
        portafolio.append(portafolio_aptitud)
    data['portafolio'] = portafolio

    print(data)
    if request.method == 'GET':
        print("get")
    else:
        return redirect('visualizar_perfil')

    return render(request, 'visualizar_perfil.html', data)


@login_required(login_url='/auth/login')
def vincular_aptitud(request,pk_aptitud,pk_user):
    data = {}
    aptitud = Aptitudes.objects.get(pk=pk_aptitud)
    user = Persona.objects.get(Usuario=pk_user)

    print("HOLA")
    print(aptitud)
    print(user)
    print("HOLA2")
    aptitud_validada = Aptitude_validadas()

    aptitud_validada.Usuario = user
    aptitud_validada.Aptitud_validada = aptitud
    aptitud_validada.save()

    if request.method =="GET":
        print("AQUI EN GET MAN")
    return "xd"
