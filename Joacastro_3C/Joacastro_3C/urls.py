"""Joacastro_3C URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from App import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.baseLogin, name='baseLogin'),
    path('Inicio', views.Inicio, name='Inicio'),
    path('Login/', views.Login, name='login'),
    path('Administrador', views.baseCrud, name='Administrador'),
    path('Listado_de_Canciones', views.Lista_canciones, name='Lista'),
    path('', views.salir, name='salir'),
    #crud 
    #Artista
    path('Crear_A/', views.Crear_Artista, name='create'),
    path('Actualizar_A/<int:id>', views.Update_Artista, name='ActualizarArtista'),
    path('ActualizarArtista/', views.actualizar_Artista, name='actualizarA'),
    path('eliminar_A/<int:id>', views.Delete_Artista, name='EliminarArtista'),

    #Albums
    path('CrearAB', views.Crear_Albums, name='createA'),
    path('Actualizar_AB/<int:id>', views.Update_Albums, name='ActualizarAlbum'),
    path('Actualizar_album/', views.actualizar_Albums, name='actualizarAl'),
    path('eliminar_AB/<int:id>/', views.Delete_Albums, name='EliminarAlbum'),

    # Canciones
    path('Crear_C', views.Crear_Cancion, name='createC'),
    path('Actualizar_C/<int:id>', views.Update_Cancion, name='ActualizarCancion'),
    path('ActualizarCancion/', views.actualizar_Cancion, name='actualizarC'),
    path('eliminar_C/<int:id>', views.Delete_Cancion, name='EliminarCancion'),

    # ver informacion mendiante el detalle
    path('Listado_de_Canciones/<int:id>', views.Informacio_cancion, name='Listado'),

    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

