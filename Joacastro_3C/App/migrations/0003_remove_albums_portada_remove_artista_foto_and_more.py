# Generated by Django 4.1.7 on 2023-03-27 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_alter_albums_portada_alter_artista_foto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='albums',
            name='portada',
        ),
        migrations.RemoveField(
            model_name='artista',
            name='foto',
        ),
        migrations.RemoveField(
            model_name='cancion',
            name='archivo_audio',
        ),
    ]
