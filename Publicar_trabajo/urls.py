from django.urls import path
from Registro_fullpega import views
from Publicar_trabajo import views

urlpatterns = [
     path('publicar_trabajo', views.publicar_trabajo, name='publicar_trabajo'),
     path('validar_aptitud', views.validar_aptitud, name='validar_aptitud'),
     path(r'^visualizar_perfil/<int:pk_user>', views.visualizar_perfil, name='visualizar_perfil'),

]
