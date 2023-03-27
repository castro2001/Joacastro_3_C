from django.shortcuts import render, redirect
from .models import Usuarios, Artista,Albums,Cancion,detalle
from django.contrib.auth import  logout
from django.contrib import messages



def Login(request):
    if request.method == 'GET':
            return render(request, 'login.html', {})
    else:
        username = request.POST.get("user")
        clave = request.POST.get("password")
        try:
            usuario = Usuarios.objects.filter(usuario= username, contrasenia= clave).first()
           
            if usuario is not None  :
            
                return render(request,'crud/inicio.html',{'user':usuario})
            else:
                 return redirect('/', {'error':  'Usuario o Contraseña no Existe!' })
                
        except Usuarios.DoesNotExist:
               return render(request,'login.html', {'error':  'Usuario o Contraseña no Existe!' })
def baseCrud(request):
    usuario = Usuarios.objects.values()
    artistas= Artista.objects.all()
    albunes= Albums.objects.all()
    canciones= Cancion.objects.all()
    mostrar= detalle.objects.all()
 
    context = {
        'listado': usuario,
        'artista': artistas,
        'album': albunes,
        'cancion': canciones,
        'detalle': detalle,
    }

    return render(request,'crud/crud.html',context)

def detalle_view(request):
    artistas= Artista.objects.all()
    albunes= Albums.objects.all()
    canciones= Cancion.objects.all()
    mostrar = detalle.objects.get(
         id_artista = artistas,
         id_canciones = canciones,
         id_albums = albunes,

    )
    context = {
        'artista': artistas,
        'album': albunes,
        'cancion': canciones,
    }
    return render(request,'crud/crud.html',context)

def Inicio(request):
    usuario = Usuarios.objects.values()
    artista = Artista.objects.values()
    return render(request,'crud/inicio.html',{'listado': usuario, 'artista':artista})

def Lista_canciones(request):
    usuario = Usuarios.objects.values()

    return render(request,'crud/lista.html',{'listado': usuario})

# Login
def baseLogin(request):
    return render(request,'login.html')

def salir(request):
    logout(request)
    return render(request,'login.html')

#codigo de CRUD
def Crear_Artista(request):
    artista= request.POST['artista']
    descripcion= request.POST['descripcion']
    fotoS= request.FILES['foto']

    crear = Artista.objects.create(
         nombre= artista,
         descripcion= descripcion,
         foto=fotoS
    )
    messages.success(request, 'Artista Creado!')
    return redirect('Administrador')

    
def Update_Artista(request,id):
    artista = Artista.objects.get(id=id)
    context={
        'artista': artista
    }

    return render(request, 'crud/actualizarArtista.html ',context)


def actualizar_Artista(request):
    id= int(request.POST['id'])
    titulo_albums= request.POST['titulo_A']
    descripcion_album= request.POST['descripcionA']
    portada_disco= request.FILES['portadaA']

    album = Artista.objects.get(id=id)
    album.nombre = titulo_albums
    album.descripcion= descripcion_album,
    album.foto =portada_disco
    album.save()
    messages.success(request, 'Album Actualizado!')
    return redirect('Administrador')

def Delete_Artista(request,id):
    album = Artista.objects.get(id=id)
    album.delete()
    messages.success(request, 'Artista Eliminado!')
    return redirect('Administrador')

#Album

def Crear_Albums(request):
    titulo_albums= request.POST['titulo_A']
    descripcion_album= request.POST['descripcionA']
    portada_disco= request.FILES['portadaA']

    crear = Albums.objects.create(
         titulo= titulo_albums,
         descripcion= descripcion_album,
         portada=portada_disco
    )
    messages.success(request, 'Album Creado!')
    return redirect('Administrador')

def Update_Albums(request,id):
    album = Albums.objects.get(id=id)
    context={
        'album': album
    }

    return render(request, 'crud/actualizar.html ',context)

def actualizar_Albums(request):
    id= int(request.POST['id'])
    titulo_albums= request.POST['titulo_A']
    descripcion_album= request.POST['descripcionA']
    portada_disco= request.POST['portadaA']

    album = Artista.objects.get(id=id)
    album.nombre = titulo_albums
    album.descripcion= descripcion_album,
    album.foto =portada_disco
    album.save()
    messages.success(request, 'Album Actualizado!')
    return redirect('Administrador')
# def actualizar_Albums(request):

def Delete_Albums(request,id):
    album = Albums.objects.get(id=id)
    album.delete()
    messages.success(request, 'Album Eliminado!')
    return redirect('Administrador')


#cancion
def Crear_Cancion(request):
    musica= request.POST['musica']
    url_musica= request.FILES['url']

    crear = Cancion.objects.create(
         titulo= musica,
         archivo_audio= url_musica
    )
    messages.success(request, 'Cancion Creado!')
  
    return redirect('Administrador')

def Update_Cancion(request,id):
    cancion = Cancion.objects.get(id=id)
    context={
        'cancion': cancion
    }

    return render(request, 'crud/actualizarCancion.html ',context)

def actualizar_Cancion(request):
    id= int(request.POST['id'])
    musica= request.POST['musica']
    url_musica= request.FILES['url']

    album = Cancion.objects.get(id=id)
    album.titulo = musica
    album.archivo_audio= url_musica,
  
    album.save()
    messages.success(request, 'Cancion Actualizada')
    return redirect('Administrador')

def Delete_Cancion(request,id):
    cancion = Cancion.objects.get(id=id)
    cancion.delete()
    messages.success(request, 'Cancion Eliminado!')
    return redirect('Administrador')


# informacion
def Informacio_cancion(request,id):
 
    info = detalle.objects.get(id=id)
    artista= info.id_artista 
    album= info.id_albums 
    canciones= info.id_canciones 
    # # artista= info.i
    context={
         'detalle':info,
         'artista':artista,
         'album':album,
         'canciones':canciones,
    }
    info.save()
    return render(request, 'crud/info.html ',context)