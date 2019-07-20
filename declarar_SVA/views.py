from django.shortcuts import render
# from Registro_SVA.models import *
# from Registro_SVA.forms import *
from declarar_SVA.models import *
from declarar_SVA.forms import *

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
def declarar_SVA(request):
    data = {}

    #data['form'] = TrabajoForm()
    data["Areas"] = Areas.objects.all()
    aptitudes = Aptitudes.objects.all()
    data['Aptitudes'] = aptitudes

    return render(request, 'declarar_SVA.html', data)

@login_required(login_url='/auth/login')
def vincular_portafolio(request,pk_aptitud):
    data = {}
    aptitud = Aptitude_validadas.objects.get(pk=pk_aptitud)
    data["aptitud"]=aptitud

    return render(request, 'vincular_portafolio.html', data)

@login_required(login_url='/auth/login')
def vincular_portafolio_save(request,pk_aptitud):
    aptitud = Aptitude_validadas.objects.get(pk=pk_aptitud)
    # aptitud = Aptitudes.objects.get(pk=pk_aptitud)
    usuario = Persona.objects.get(Usuario=request.user.pk)


    # portafolio = Portafolio()
    # portafolio.aptitude_validadas = aptitud

    print(request)
    data = {}
    print("HOLA")
    if request.method == 'GET':
        print("get")
    if request.method == 'POST':
        #primero tengo que crear la aptitud vinculadada


        print("POSSST BEIBE")
        print(request.POST)
        nombre = request.POST["nombre_aptitud"]
        file = request.POST["file_aptitud"]
        print(type(file))
        portafolio = Portafolio()
        portafolio.Usuario = usuario
        portafolio.aptitude_validadas = aptitud
        portafolio.Nombre = nombre
        if (file == ""):
            print("esta vacio we")
        else:
            portafolio.pdf = "pdf/"+file
        portafolio.save()
    # return render(request, 'visualizar_perfil.html', data)
    return redirect('visualizar_perfil',1)



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
    # print(usuario.pk)
    # print(request.user.pk)
    data['aptidudes_validadas'] = Aptitude_validadas.objects.filter(Usuario=usuario.pk)
    print(data['aptidudes_validadas'])
    portafolio=[]
    #portafolio
    for i in data['aptidudes_validadas']:
        # print("en for")
        print(i.pk)
        # print(i.Aptitud_validada.pk)
        portafolio_aptitud= Portafolio.objects.filter(aptitude_validadas = i.pk)
        #print(portafolio_aptitud)
        portafolio.append(portafolio_aptitud)
    data['portafolio'] = portafolio

    # print(data)
    if request.method == 'GET':
        print("get")
    else:
        return redirect('visualizar_perfil')
    print(data)
    return render(request, 'visualizar_perfil.html', data)


@login_required(login_url='/auth/login')
def vincular_aptitud(request,pk_aptitud,pk_user):
    data = {}
    aptitud = Aptitudes.objects.get(pk=3)
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
