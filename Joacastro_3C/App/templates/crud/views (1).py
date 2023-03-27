from django.shortcuts import render, redirect
from PokedexAPP.models import Usuario, Region, Pokemon, Rutas, Pokedex  
from django.db.models import Q
from django.core.cache import cache




def inicioDef(request):
    return render(request, 'inicio.html', {})

def perfilDef (request,id):
    usuario= Usuario.objects.get(id=id)
    context = {'usuario': usuario}
    return render(request, 'perfil.html', context)
def paginaDef(request):
    nomUsuario = cache.get('nomUsuario')
    context = {'nomUsuario': nomUsuario}
    return render(request, 'index.html',context)
def registroDef (request):
    return render (request, 'Registro.html', {})

def regionDef (request):
    regiones = Region.objects.all()
    nomUsuario = cache.get('nomUsuario')
  
    context = {'regiones': regiones,
        'nomUsuario': nomUsuario
    }
    return render (request, 'region.html', context )


def pokemonDef (request):
    nomUsuario = cache.get('nomUsuario')
    pokemon = Pokemon.objects.all()
    context = {'pokemon': pokemon,
               'nomUsuario': nomUsuario }
    return render (request, 'pokemon.html', context )


def  buscadorVistaDef (resquest):
    nomUsuario = cache.get('nomUsuario')
    context = { 'nomUsuario': nomUsuario }
    return render (resquest, 'buscador.html',context)

def rutasDef(resquest, ):
    nomUsuario = cache.get('nomUsuario')
    rutas = Rutas.objects.all()
    context = {'rutas': rutas, 'nomUsuario': nomUsuario }
    return render (resquest,'rutas.html',context)


def pokedexDef(request):
    nomUsuario = cache.get('nomUsuario')
    rutas = Rutas.objects.all()
    regiones = Region.objects.all()
    pokemon = Pokemon.objects.all()
    pokedex = Pokedex.objects.all()
    context = {
        'rutas':rutas,
        'regiones': regiones,
        'pokemon': pokemon,
        'pokedex': pokedex,
        'nomUsuario': nomUsuario
    }
  
    return render(request, 'pokedex.html', context)



def LoginSesionDef(request):
    if request.method == 'GET':
        return render(request, 'inicio.html', {})
    else:
        usuarioSTR = request.POST.get("userInTx")
        ContraSTR = request.POST.get("passwordInPs")
        usuario = Usuario.objects.filter(usuario=usuarioSTR, contraseña=ContraSTR).first()
        if usuario is not None:
            nomUsuario = usuario.usuario
            cache.set ('nomUsuario', nomUsuario)

            context = {'usuario': usuario, 'nomUsuario': nomUsuario}
            return render(request, 'pagina.html', context)
        else:
            return render(request, 'inicio.html')

def registroUsuarioDef(request):
    nombre = request.POST['nombre']
    apellido = request.POST['apellido']
    email = request.POST['email']
    contraseña = request.POST['contraseña']
    fecha_nacimiento = request.POST['fecha_nacimiento']
    usuario_input = request.POST['usuario']

    usuario = Usuario.objects.create(
        nombre = nombre,  apellido= apellido,
        email = email, contraseña = contraseña,
        fecha_nacimiento = fecha_nacimiento,
        usuario =  usuario_input
    )

    return redirect('/' )

def pokemonRegistroDef (request):
    nombre = request.POST['nombrePokemon']
    numero_pokedex = request.POST['numero_pokedex']
    descripcion = request.POST['descripcionPokemon']
    tipos = request.POST['tipoPokemon']
    evolucion = request.POST['evolucion']
    pokemon = Pokemon.objects.create(
        nombre = nombre, numero_pokedex= numero_pokedex,
        descripcion = descripcion , tipos =tipos,
        evolucion =evolucion 
    )
    return redirect('pokemonUrl')

def capturarPokemonDef(request, id):
    pokemon = Pokemon.objects.get(id = id)
    return render(request, "editar_pokemon.html", {'pokemon': pokemon} )

def actualizar_PokemonDef(request):
  
    id = request.POST['id_pokemon']
    nombre = request.POST['nombrePokemon']
    numero_pokedex = request.POST['numero_pokedex']
    descripcion = request.POST['descripcionPokemon']
    tipos = request.POST['tipoPokemon']
    evolucion = request.POST['evolucion']
      
    pokemon = Pokemon.objects.get(id = id)
    pokemon.nombre = nombre
    pokemon.numero_pokedex = numero_pokedex
    pokemon.descripcion = descripcion
    pokemon.tipos = tipos
    pokemon.evolucion =evolucion

    pokemon.save()
   

    return redirect('pokemonUrl')

def EliminarPokemon(request, id):
    pokemon = Pokemon.objects.get(id = id)
    pokemon.delete()
    return redirect('pokemonUrl')


def regionRegistroDef (request):
    nombre = request.POST['nombreRegion']
    generacion = request.POST['Generacion']
    fecha_salida = request.POST['salida']
    consola = request.POST['consola']
    descripcion = request.POST['descripcion']

    region = Region.objects.create(
        nombre = nombre, generacion = generacion,
        fecha_salida = fecha_salida, consola =consola,
        descripcion = descripcion

    )
    return redirect('regionUrl')

def capturarRegionDef(request, id):
    region = Region.objects.get(id = id)
    return render(request, "editar_region.html", {'region': region} )

def actualizar_regionDef(request):
  

    id = request.POST.get('id_region')
    nombre = request.POST.get('nombre')
    generacion = request.POST.get('generacion')
    fecha_salida = request.POST.get('fecha_salida')
    consola = request.POST.get('consola')
    descripcion = request.POST.get('descripcion')
      
    region = Region.objects.get(id=id)
    
    region.nombre = nombre
    region.generacion = generacion
    region.fecha_salida = fecha_salida
    region.consola = consola
    region.descripcion = descripcion

    region.save()
   

    return redirect('regionUrl')

def eliminarRegionDef(request, id):
    region = Region.objects.get(id = id)
    region.delete()
    return redirect('regionUrl')
    


def crearRutasDef (request):
    nombre = request.POST['nombreRuta']
    ubicacion = request.POST['ubicacionRuta']
    tipo = request.POST['tipoRuta']
  

    region = Rutas.objects.create(
        nombre = nombre, ubicacion = ubicacion,
        tipo = tipo,      

    )

    return redirect('rutasUrl')


def capturarRutaDef(resquest, id):
    rutas = Rutas.objects.get(id = id)
    return render(resquest, "editar_rutas.html", {'rutas': rutas} )

def editarRutasDef(resquest):
    id = resquest.POST['id_ruta']
    nombre = resquest.POST['nombreRuta']
    ubicacion = resquest.POST['ubicacionRuta']
    tipo = resquest.POST['tipoRuta']

    rutas = Rutas.objects.get (id = id)

    rutas.nombre = nombre
    rutas.ubicacion = ubicacion
    rutas.tipo = tipo

    rutas.save()

    return redirect('rutasUrl')

def eliminarRutaDef(request, id):
    rutas = Rutas.objects.get(id = id)
    rutas.delete()
    return redirect('regionUrl')

def crearPokedex(resquest):
    pokemon = Pokemon.objects.get(pk=resquest.POST['id_pokemon'])
    rutas = Rutas.objects.get(pk=resquest.POST['id_rutas'])
    region = Region.objects.get(pk=resquest.POST['id_region'])

    pokedex = Pokedex.objects.create(
        id_region = region, id_rutas =rutas,
        id_pokemon =pokemon
    )

    return redirect('pokedexUrl')

def capturarPokedexDef(resquest, id):
    pokedex = Pokedex.objects.get(id = id)
    rutas = Rutas.objects.all()
    regiones = Region.objects.all()
    pokemon = Pokemon.objects.all()

    context = {
        'rutas':rutas,
        'regiones': regiones,
        'pokemon': pokemon,
        'pokedex': pokedex
    }

    return render(resquest, "editar_pokedex.html",context )

def editarPokedexDef(resquest):
    id = resquest.POST['id_pokedex']
    pokemon = Pokemon.objects.get(pk=resquest.POST['id_pokemon'])
    rutas = Rutas.objects.get(pk=resquest.POST['id_rutas'])
    region = Region.objects.get(pk=resquest.POST['id_region'])

    pokedex = Pokedex.objects.get(id = id)

    pokedex.id_pokemon= pokemon
    pokedex.id_region =  region
    pokedex.id_rutas = rutas

    pokedex.save()

    return redirect('pokedexUrl')
def eliminarPokedexDef(request, id):
    pokedex = Pokedex.objects.get(id = id)
    pokedex.delete()
    return redirect('pokedexUrl')





def buscadorDef(request):
    if request.method == 'GET':
        nomUsuario = cache.get('nomUsuario')
        search_query = request.GET.get('search_query')

        regions = Region.objects.filter(Q(nombre__icontains=search_query) | 
            Q(generacion__icontains=search_query) | 
            Q(consola__icontains=search_query) | 
            Q(descripcion__icontains=search_query)
        )

        rutas = Rutas.objects.filter(Q(nombre__icontains=search_query) | 
         Q(ubicacion__icontains=search_query) | 
         Q(tipo__icontains=search_query)
        )

        pokemons = Pokemon.objects.filter(Q(nombre__icontains=search_query) | 
            Q(numero_pokedex__icontains=search_query) | 
            Q(descripcion__icontains=search_query) | 
            Q(tipos__icontains=search_query)
        )

        pokedexs = Pokedex.objects.filter(id_pokemon__in=pokemons, 
            id_rutas__in=rutas, 
            id_region__in=regions
        )

        context = {
            'regions': regions,
            'rutas': rutas,
            'pokemons': pokemons,
            'pokedexs': pokedexs,
            'nomUsuario': nomUsuario
        }
        return render(request, 'buscador_resultado.html', context)

