from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', include('Registro_SVA.urls'), name='Registro_SVA'),
    path('auth/', include('Auth_SVA.urls'), name='auth'),
    path('publicar/', include('declarar_SVA.urls'), name='auth'),

    # path("index_SVA/", include('SVA.urls'), name='SVA'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
