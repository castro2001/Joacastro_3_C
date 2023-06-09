# Generated by Django 4.1.7 on 2023-03-27 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Albums',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150, verbose_name='Titulo del Album')),
                ('descripcion', models.CharField(max_length=300, verbose_name='Descripcion del Album')),
                ('portada', models.FileField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Artista',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150, verbose_name='Nombre del Artista')),
                ('descripcion', models.CharField(max_length=300, verbose_name='Descripcion')),
                ('foto', models.FileField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Cancion',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150, verbose_name='Titulo de la Cancion')),
                ('archivo_audio', models.FileField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('fecha_creacion', models.DateField(auto_created=True, verbose_name='Fecha de Creacion')),
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('usuario', models.CharField(max_length=20, verbose_name='Usuario')),
                ('contrasenia', models.IntegerField(verbose_name='Contraseña')),
            ],
        ),
        migrations.CreateModel(
            name='detalle',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID')),
                ('id_albums', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.albums')),
                ('id_artista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.artista')),
                ('id_canciones', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.cancion')),
            ],
        ),
    ]
