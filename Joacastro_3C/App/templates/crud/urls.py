
from django.urls import path
from PokedexAPP import views

urlpatterns = [
    path('',views.inicioDef, name='inicioUrl'),
    path('pagina/', views.paginaDef, name='paginaUrl'),
    path('perfil/<int:id>',views.perfilDef, name='perfilUrl'),
    path('registro',views.registroDef, name='registroUrl'),
    path('loginAction/',views.LoginSesionDef, name='loginUrl'),
    path('region/',views.regionDef, name='regionUrl'),    
    path('pokemon/',views.pokemonDef, name='pokemonUrl'),    
    path('rutas/',views.rutasDef, name='rutasUrl'),  
    path('pokedex/',views.pokedexDef, name='pokedexUrl'), 

    path('createPokedex/',views.crearPokedex, name='crearPokedexUrl'), 
    path('registroAction/',views.registroUsuarioDef, name='funcioRegistroUrl'),
    path('regionCreate/',views.regionRegistroDef, name='crearRegionUrl'),
    path('region_actualizar', views.actualizar_regionDef, name='detalle_region') ,
    path('actualizar/<int:id>/', views.capturarRegionDef, name='actualizar_region'), 
    path('EliminarRegion/<int:id>/', views.eliminarRegionDef, name='Eliminar_region'),
    path('pokemonCreate/',views.pokemonRegistroDef, name='CrearPokemonUrl'),
    path('actualizarPokemon/<int:id>',views.capturarPokemonDef, name='pokemonActualizar'),
    path('pokemon_region/',views.actualizar_PokemonDef, name='pokemonActualizarUrl'),
    path('eliminarPokemon/<int:id>/', views.EliminarPokemon, name='Eliminar_pokemon'),
    path('CrearRutas/',views.crearRutasDef, name='CrearRuta'),  
    path('CapturarRuta/<int:id>',views.capturarRutaDef, name='CapturarRuta'),
    path('actualizarRuta/',views.editarRutasDef, name='actualizarRuta'),  
    path('eliminarRutas/<int:id>',views.eliminarRutaDef, name='eliminarRuta'), 
    path('CapturarPokedex/<int:id>',views.capturarPokedexDef, name='CapturarPokedex'),
    path('actualizarPokedex/',views.editarPokedexDef, name='actualizarPokedex'),  
    path('eliminarPokedex/<int:id>',views.eliminarPokedexDef, name='eliminarPokedex'),  
    path('buscar/', views.buscadorVistaDef, name='buscador') ,
    path('buscador_resultado/', views.buscadorDef, name='buscador_resultado'),     
]
