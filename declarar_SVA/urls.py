from django.urls import path
from Registro_SVA import views
from declarar_SVA import views
from . import views
from django.conf.urls import url

urlpatterns = [
     path('declarar_SVA', views.declarar_SVA, name='declarar_SVA'),
     path(r'^vincular_portafolio/<int:pk_aptitud>', views.vincular_portafolio, name='vincular_portafolio'),
     path(r'^vincular_portafolio_save/<int:pk_aptitud>', views.vincular_portafolio_save, name='vincular_portafolio_save'),
     path(r'^validar_aptitud/<int:pk_aptitud>', views.validar_aptitud, name='validar_aptitud'),
     path(r'^visualizar_perfil/<int:pk_user>', views.visualizar_perfil, name='visualizar_perfil'),
     path(r'^vincular_aptitud/<int:pk_aptitud>/subpage/<int:pk_user>', views.vincular_aptitud, name='vincular_aptitud'),

]
