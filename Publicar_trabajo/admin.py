from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
# Register your models here.



@admin.register(Direccion)
class DireccionAdmin(admin.ModelAdmin):
    list_display = ('Comuna','Pais','Ciudad','Calle','Numero_de_calle')

@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('pk','Usuario','Nombre','Rut','Imagen','Telefono_C','Correo','Direccion')

@admin.register(Aptitudes)
class AptitudesAdmin(admin.ModelAdmin):
    list_display = ('Area','Nombre','Descripccion','Fecha')
@admin.register(Respuestas)
class RespuestasAdmin(admin.ModelAdmin):
     list_display = ('Usuario','Informacion','Validez','list_display')
@admin.register(Pregunta)
class PreguntaAdmin(admin.ModelAdmin):
    list_display = ('pk','pregunta','a','b','c','d',)
@admin.register(Cuestionario)
class CuestionarioAdmin(admin.ModelAdmin):
    list_display = ('Aptitud_vinculada',)

@admin.register(Areas)
class AreasAdmin(admin.ModelAdmin):
    list_display = ('Nombre',)