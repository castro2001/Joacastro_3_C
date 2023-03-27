from django.contrib import admin
from .models import Usuarios, Artista, Cancion,Albums,detalle
# Register your models here.
admin.site.register(Usuarios)
admin.site.register(Artista)
admin.site.register(Albums)
admin.site.register(Cancion)
admin.site.register(detalle)