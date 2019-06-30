from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe
# Register your models here.



@admin.register(Direccion)
class DireccionAdmin(admin.ModelAdmin):
    list_display = ('Comuna','Pais','Ciudad','Estado')

@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('Usuario','Nombre','Rut','Imagen','Telefono_C','Correo','Direccion')

@admin.register(Aptitudes)
class AptitudesAdmin(admin.ModelAdmin):
    list_display = ('Area','Nombre','Descripccion','Fecha')
@admin.register(Respuestas)
class RespuestasAdmin(admin.ModelAdmin):
     list_display = ('Usuario','Informacion','Validez','list_display')
@admin.register(Pregunta)
class PreguntaAdmin(admin.ModelAdmin):
    list_display = ('Descripcion','Respuestas','Usuario')
@admin.register(Cuestionario)
class CuestionarioAdmin(admin.ModelAdmin):
    list_display = ('Preguntas',)

@admin.register(Areas)
class AreasAdmin(admin.ModelAdmin):
    list_display = ('Nombre',)