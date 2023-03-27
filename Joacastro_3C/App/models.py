from django.db import models

# Create your models here.
class Usuarios(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    usuario = models.CharField(verbose_name='Usuario', max_length=20)
    contrasenia = models.IntegerField(verbose_name='Contraseña')
    fecha_creacion = models.DateField(verbose_name='Fecha de Creacion', auto_created=True)

    def __str__(self) :
        return f'Usuario: {self.usuario} || contraseña : {self.contrasenia}'

class Artista(models.Model):
    id = models.IntegerField( primary_key=True, verbose_name='ID')
    nombre = models.CharField(verbose_name='Nombre del Artista', max_length=150)
    descripcion = models.CharField(verbose_name='Descripcion', max_length=300)
    foto = models.FileField(upload_to='images/', null=True, blank=True)

  

class Albums(models.Model):
    id = models.IntegerField( primary_key=True, verbose_name='ID')
    titulo = models.CharField(verbose_name='Titulo del Album', max_length=150, null=False    )
    descripcion = models.CharField(verbose_name='Descripcion del Album', max_length=300)
    portada = models.FileField(upload_to='images/', null=True, blank=True)
    
class Cancion(models.Model):
    id = models.IntegerField( primary_key=True, verbose_name='ID')
    titulo = models.CharField(verbose_name='Titulo de la Cancion', max_length=150)
    archivo_audio = models.FileField(upload_to='images/', null=True, blank=True) # campo para subir el archivo de audio
    # album = models.CharField(verbose_name='Titulo de la Cancion', max_length=150)
    
class detalle (models.Model):
    id = models.IntegerField( primary_key=True, verbose_name='ID')
    id_artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    id_canciones = models.ForeignKey(Cancion, on_delete=models.CASCADE)
    id_albums = models.ForeignKey(Albums, on_delete=models.CASCADE)
