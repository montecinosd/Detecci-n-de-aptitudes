from datetime import date,datetime
from Registro_SVA.models import *

from django.db import models



from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

# Create your models here.
def content_file_name(instance, filename):
    return '/'.join(['content', instance.Usuario.username, filename])
def content_file_document(instance, filename):
    return '/'.join(['document', instance.Usuario.username, filename])

class Areas(models.Model):
    Nombre = models.CharField(max_length=120)

class Direccion(models.Model):
    Comuna = models.CharField(max_length = 50, null=True,blank=True)
    Pais = models.CharField(max_length = 50, null=True,blank=True)
    Ciudad = models.CharField(max_length = 50,null=True,blank=True)
    Calle = models.CharField(max_length=100,null=True,blank=True)
    Numero_de_calle = models.CharField(max_length=100,null=True,blank=True)
class Persona(models.Model):
    Usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    Nombre = models.CharField(max_length = 120,null=True,blank=True)
    Rut = models.CharField(max_length=20,null=True,blank=True)
    Imagen = models.ImageField(upload_to=content_file_name,null=True,blank=True)
    Telefono_C = models.CharField(max_length = 50,null=True,blank=True)
    Correo = models.CharField(max_length = 100,null=True,blank=True)
    Direccion = models.OneToOneField(Direccion, on_delete=models.CASCADE)



class Aptitudes(models.Model):
    Usuario = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    Area = models.ForeignKey(Areas, on_delete=models.CASCADE)
    Imagen = models.ImageField(upload_to=content_file_name,null=True,blank=True)
    Nombre = models.CharField(max_length = 120,null=True,blank=True)
    Descripccion = models.TextField()
    Fecha = models.DateTimeField(default=timezone.now)

class Aptitude_validadas(models.Model):
    Usuario = models.ForeignKey(Persona, on_delete=models.CASCADE)
    Aptitud_validada = models.ForeignKey(Aptitudes, on_delete=models.CASCADE)


class Cuestionario(models.Model):
    Aptitud_vinculada = models.ForeignKey(Aptitudes, on_delete=models.CASCADE)

class Portafolio(models.Model):
    Nombre = models.CharField(max_length = 50,null=True,blank=True)
    Usuario = models.ForeignKey(Persona, on_delete=models.CASCADE)
    aptitude_validadas = models.ForeignKey(Aptitude_validadas, on_delete=models.CASCADE,null=True,blank=True)
    pdf = models.FileField(upload_to='pdf')

class Pregunta(models.Model):
    pregunta = models.CharField(max_length = 100,null=True,blank=True)
    a =  models.CharField(max_length = 100,null=True,blank=True)
    b =  models.CharField(max_length = 100,null=True,blank=True)
    c =  models.CharField(max_length = 100,null=True,blank=True)
    d =  models.CharField(max_length = 100,null=True,blank=True)
    Cuestionario = models.ForeignKey(Cuestionario, on_delete=models.CASCADE)
    Aptitud_vinculada = models.ForeignKey(Aptitudes, on_delete=models.CASCADE)
    Respuesta_correcta = models.CharField(max_length = 10,null=True,blank=True)

    #Respuestas = models.ForeignKey(Respuestas, on_delete=models.CASCADE,null=True,blank=True)
    Usuario = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
